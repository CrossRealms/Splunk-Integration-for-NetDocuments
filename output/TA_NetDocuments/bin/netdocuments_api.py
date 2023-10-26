
import sys
import requests
import json


class NetDocuments:
    def __init__(self, logger, account_details, proxy_settings=None):
        self.logger = logger
        self.account_details = account_details
        self.proxy_settings = proxy_settings
        self.access_token = None

        self.base_url = f'https://api.{self.account_details.endpoint}/v1/'
        self.token_refresh_url = f'https://api.{self.account_details.endpoint}/v1/OAuth'
        self.logger.debug("NetDocuments class initialized.")


    # TODO - Need to update the access token inside the account.conf file - See lansweeper's update_access_token() function for reference

    def get_access_token(self):
        if self.access_token:
            return self.access_token

        username = f"{self.account_details.client_id}|{self.account_details.repository_id}"
        password = self.account_details.client_secret

        # Define the token URL
        token_url = f'https://api.{self.account_details.endpoint}/v1/OAuth'

        data = {
            "grant_type": "client_credentials",
            "scope": self.account_details.scope,
        }

        headers = {
            # "Authorization": authorization_header,
            "Content-Type": "application/x-www-form-urlencoded",  # URL-encoded form data
            "Accept": "application/json",
        }

        # Send the POST request
        response = requests.post(token_url, auth=requests.auth.HTTPBasicAuth(username, password), data=data, headers=headers)

        if response.status_code == 200:
            # Parse the JSON response
            response_data = response.json()
            access_token = response_data.get("access_token")
            token_type = response_data.get("token_type")

            self.logger.debug(f"Token Type: {token_type}")
            self.access_token = access_token
            return access_token
        else:
            self.logger.error(f"Request for getting access token failed with status code {response.status_code}. Response_text={response.text}")


    def refresh_the_access_token(self):
        """
        Refreshes the access token once it is expired
        return status code of the API call and the response
        """
        self.logger.info('Refreshing the access token to get the fresh token')

        data = {"client_id": self.account_details.client_id, "client_secret": self.account_details.client_secret,
                "grant_type": "refresh_token", "refresh_token": self.account_details.refresh_token}
        try:
            response = requests.post(
                url=self.token_refresh_url, data=data, proxies=self.proxy_settings)

            if response.status_code == 200:
                response_json = response.json()
                self.access_token = response_json.get('access_token')
                self.logger.info('Successfully refreshed the access token.')
                return True

            self.logger.error(
                'Error while refreshing the access token, status code={} response={}'.format(response.status_code, response.text))

        except Exception as exception:
            self.logger.exception(
                'Error while refreshing the access token, error={}'.format(exception))

        return False


    def is_token_expired(self, prev_api_response):
        """
        Checks if the access token is
        param status_code: status code of the API response
        param response: Response text of the API response
        return Refreshed access_token and the refresh_token in case the token is expired, and false otherwise
        """
        try:
            # response_json = json.loads(prev_api_response.text)
            self.logger.debug('Checking if the access token is expired')

            if prev_api_response.status_code == 401:
            #  and ((response.get('errors', [])[0].get('extensions', {}).get('code') == 'UNAUTHENTICATED') or (response.get('errors', [])[0].get('extensions', {}).get('extensions', {}).get('code') == 'UNAUTHENTICATED')):
                self.logger.info('Access token is expired.')
                self.logger.info(f'prev_api_response.text = {prev_api_response.text}')
                return True
            else:
                self.logger.warning("Non 401 status code. status_code={}, response={}".format(prev_api_response.status_code, prev_api_response.response))

        except Exception as exception:
            self.logger.exception(
                'Error while checking if the access token is expired, error={}'.format(exception))
        return False


    def make_api_call_for_oauth(self, url, method="GET", params=None, data=None):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self.account_details.access_token}
        full_url = f'{self.base_url.rstrip("/")}/{url.lstrip("/")}'

        try:
            self.logger.debug("Request for URL={}".format(full_url))
            response = requests.request(method, full_url, params=params, json=data, headers=headers, proxies=self.proxy_settings)
            status_code = response.status_code

            self.logger.debug("API Call Response to URL={}: status_code:{}, response_text:{}".format(full_url, status_code, response.text))

            if response.ok:
                return response

            self.logger.warning('Error while making the API call to URL={}, status_code={}'.format(full_url, status_code))
            is_access_token_expired = self.is_token_expired(response)
            if is_access_token_expired:
                is_refreshed_token = self.refresh_the_access_token()

                if is_refreshed_token:
                    response2 = requests.request(method, full_url, params=params, json=data, headers=headers, proxies=self.proxy_settings)
                    status_code2 = response2.status_code

                    self.logger.debug("After refreshing the access token, API Call Response to URL={}: status_code:{}, response_text:{}".format(full_url, status_code2, response2.text))
                    return response2

        except Exception as exception:
            self.logger.exception(
                'Error while making the API call to URL={}, error={}'.format(full_url, exception))
            return False


    def make_api_call(self, url, method="GET", params=None, data=None):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self.get_access_token()}
        full_url = f'{self.base_url.rstrip("/")}/{url.lstrip("/")}'

        try:
            self.logger.debug("Request for URL={}".format(full_url))
            response = requests.request(method, full_url, params=params, json=data, headers=headers, proxies=self.proxy_settings)
            status_code = response.status_code

            self.logger.debug("API Call Response to URL={}: status_code:{}, response_text:{}".format(full_url, status_code, response.text))

            if response.ok:
                return response
            else:
                self.logger.error('Error while making the API call to URL={}, status_code={}'.format(full_url, status_code))
                return response

        except Exception as exception:
            self.logger.exception(
                'Error while making the API call to URL={}, error={}'.format(full_url, exception))
            return False
