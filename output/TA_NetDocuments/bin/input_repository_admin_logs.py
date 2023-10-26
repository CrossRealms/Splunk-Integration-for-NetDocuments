
import json
from datetime import datetime, timedelta
from splunklib import modularinput as smi

from addon_helper import AddonInput
from netdocuments_api import NetDocuments


class RepositoryAdminLog(AddonInput):
    def collect(self, account_details, proxy_settings, input_name, input_item, last_checkpoint):
        sourcetype = "netdocuments:repository:admin:logs"

        netdocs_api = NetDocuments(self.logger, account_details)

        if not last_checkpoint:
            now = datetime.now()
            seven_days_ago = now - timedelta(days=1)  # update limit
            last_checkpoint = seven_days_ago.strftime("%Y-%m-%dT%H:%M:%SZ")

        repository_id = account_details.get('repository_id')
        response = netdocs_api.make_api_call(f'Repository/{repository_id}/log', params={"start_date": last_checkpoint, "Logtype": "admin", "format": "json"})

        self.logger.info("Completed the HTTP request to RepositoryAdminLog.")

        if response:
            if response.status_code == 200:
                cleaned_response_text = response.text.lstrip('\ufeff')
                json_data = json.loads(cleaned_response_text)
                for line in json_data:
                    self.event_writer.write_event(
                        smi.Event(
                            data=json.dumps(line['activity'], ensure_ascii=False, default=str),
                            index=input_item.get("index"),
                            sourcetype=sourcetype,
                        )
                    )
                self.logger.info(f'Ingested {len(json_data)} for input="{input_name.split("/")[-1]}" in the sourcetype="{sourcetype}"')
                return "new_value"   # return updated checkpoint

            else:
                self.logger.error(f"Unable to fetch admin data from repository={repository_id}, status_code={response.status_code}")
