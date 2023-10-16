
import sys
import requests
import json


class NetDocuments:
    def __init__(self, logger, account_details, proxy_settings=None):
        """
        Initialization of the NetDocuments properties
        :param client_id: Client ID of the NetDocuments Account
        :param client_secret: Client Secret of the NetDocuments Account
        :param access_token: Access Token of the NetDocuments Account
        :param refresh_token: Refresh Token of the NetDocuments Account
        :param logger: Logger object
        :param proxy_settings: Proxy settings configured by the user
        """
        endpoint = account_details.get('endpoint')
        self.client_id = account_details.get('client_id')
        self.client_secret = account_details.get('client_secret')
        self.access_token = account_details.get('access_token')
        self.refresh_token = account_details.get('refresh_token')

        self.proxy_settings = proxy_settings

        self.base_url = f'https://api.{endpoint}/v1/'
        self.token_refresh_url = f'https://api.{endpoint}/v1/OAuth'
        self.logger = logger
        self.logger.debug("NetDocuments class initialized.")


    def refresh_the_access_token(self):
        """
        Refreshes the access token once it is expired
        return status code of the API call and the response
        """
        self.logger.info('Refreshing the access token to get the fresh token')

        data = {"client_id": self.client_id, "client_secret": self.client_secret,
                "grant_type": "refresh_token", "refresh_token": self.refresh_token}
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


    def make_api_call(self, url, method="GET", params=None, data=None):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self.access_token}
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
