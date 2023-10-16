
import json
from splunklib import modularinput as smi

from addon_helper import AddonInput
from netdocuments_api import NetDocuments


class RepositoryUserLog(AddonInput):
    def collect(self, account_details, proxy_settings, input_name, input_item, last_checkpoint):
        sourcetype = "netdocuments:repository:user:logs"

        client_id = account_details.get('client_id')
        client_secret = account_details.get('client_secret')
        access_token = account_details.get('access_token')
        refresh_token = account_details.get('refresh_token')

        netdocs_api = NetDocuments(self.logger, client_id=client_id, client_secret=client_secret, access_token=access_token, refresh_token=refresh_token)

        repository_id = input_item.get('repository_id')
        response = netdocs_api.make_api_call(f'/v1/Repository/{repository_id}/log', params={"start_date": last_checkpoint, "Logtype": "consolidated", "format": "json"})

        if response.status_code == 200:

            res_json = response.json()
            for line in res_json:
                self.event_writer.write_event(
                    smi.Event(
                        data=json.dumps(line, ensure_ascii=False, default=str),
                        index=input_item.get("index"),
                        sourcetype=sourcetype,
                    )
                )
            self.logger.info(f'Ingested {len(res_json)} for input="{input_name.split("/")[-1]}" in the sourcetype="{sourcetype}"')
            return "new_value"   # return updated checkpoint

        else:
            self.logger.error(f"Unable to fetch user data from repository={repository_id}, status_code={response.status_code}")

# format supported yyyy-MM-ddThh:mm:ssZ - for checkpoint and start_date
