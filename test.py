# Scope
# possible scopes
'''
read – read all data the user has rights to access
edit - upload document content, create versions, check out, check in, change official version, create or modify document attachments
organize – create folders and saved searches, file items in folders, manipulate ACLs and profile values, manipulate favorite lists, home page, and recent docs lists, change folder parent
lookup – insert, update, and delete lookup table rows
delete doc – delete documents
delete container – delete folders, saved searches, filters, and workspaces
full – full access to all resources.  The application is permitted to do everything the user has rights to do.
admin – needed for repository user list and group list along with the read permission
'''


# Client Credentials Grant Flow

# Define your client ID, client secret, and repository ID
# 2023-10-26
client_id = "AP-PVNONB11"
client_secret = "9Ti3vgFI5r6H2wxR6rLSXcTzHPSdWNPXHaVnzOXOKzdDCKez"


import requests

repository_id = "CA-P8KZQ4F3"

# Construct the client credentials header
# credentials = f"{client_id}|{repository_id}:{client_secret}"
# base64_credentials = base64.b64encode(credentials.encode()).decode()
# authorization_header = f"Basic {base64_credentials}"
username = f"{client_id}|{repository_id}"
password = client_secret

# Define the token URL
token_url = "https://api.vault.netvoyage.com/v1/OAuth"

# Define the request parameters
data = {
    "grant_type": "client_credentials",
    "scope": "read full",  # Add your desired scopes here
}


# Define the headers, including the Authorization header
headers = {
    "Content-Type": "application/x-www-form-urlencoded",  # URL-encoded form data
    "Accept": "application/json",  # Specify JSON response
}

# Send the POST request
response = requests.post(token_url, auth=requests.auth.HTTPBasicAuth(username, password), data=data, headers=headers)


base_url = f'https://api.vault.netvoyage.com/v1/'

def make_api_call(access_token, url, method="GET", params=None, data=None):
    headers = {'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token}
    full_url = f'{base_url.rstrip("/")}/{url.lstrip("/")}'

    print("Full URL of HTTP request = {}".format(full_url))

    try:
        response = requests.request(method, full_url, params=params, json=data, headers=headers, proxies=None, timeout=280)
        status_code = response.status_code

        print("API Call Response to URL={}: status_code:{}".format(full_url, status_code))

        if response.ok:
            return response
        else:
            print('Error while making the API call to URL={}, status_code={}'.format(full_url, status_code))
            return response

    except Exception as exception:
        print(
            'Error while making the API call to URL={}, error={}'.format(full_url, exception))
        return False


# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    access_token = response_data.get("access_token")
    token_type = response_data.get("token_type")
    
    # You can now use the access token in your API requests
    print(f"Access Token: {access_token}")
    print(f"Token Type: {token_type}")

    last_checkpoint = "2023-10-30T19:18:46Z"

    response = make_api_call(access_token=access_token, url=f'Repository/{repository_id}/log', params={"start_date": last_checkpoint, "Logtype": "admin", "format": "json"})

    print(f"response.status_code={response.status_code}, response.text={response.text}")

else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # Print the response content for debugging

