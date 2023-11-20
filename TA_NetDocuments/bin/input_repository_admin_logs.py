
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
        response = netdocs_api.make_api_call(f'Repository/{repository_id}/log', params={"start": last_checkpoint, "Logtype": "admin", "format": "json"})

        self.logger.info("Completed the HTTP request to RepositoryAdminLog.")

        if response:
            if response.status_code == 200:
                cleaned_response_text = response.text.lstrip('\ufeff')
                json_data = json.loads(cleaned_response_text)
                self.logger.debug("json_data response: {}".format(json_data))

                last_date = json_data[-1]['activity']['date']

                self.logger.debug(f'Total events fetched from API {len(json_data)}')
                self.logger.debug(f'Last event fetched from API with date="{last_date}"')

                for e in json_data:
                    self.event_writer.write_event(
                        smi.Event(
                            data=json.dumps(e['activity'], ensure_ascii=False, default=str),
                            index=input_item.get("index"),
                            sourcetype=sourcetype,
                        )
                    )

                self.logger.info(f'Ingested {len(json_data)} events for input="{input_name.split("/")[-1]}" in the sourcetype="{sourcetype}"')

                _last_data_obj = datetime.strptime(last_date, "%Y-%m-%dT%H:%M:%S")
                _last_data_obj = _last_data_obj + timedelta(seconds=1)
                next_checkpoint = _last_data_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
                self.logger.info(f'Next checkpoint start date for input="{input_name.split("/")[-1]}" is next_start_date="{next_checkpoint}"')
                return next_checkpoint

            else:
                self.logger.error(f"Unable to fetch admin data from repository={repository_id}, status_code={response.status_code}")
