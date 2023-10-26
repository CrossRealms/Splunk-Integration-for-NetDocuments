
import json
from datetime import datetime, timedelta
from splunklib import modularinput as smi

from addon_helper import AddonInput
from netdocuments_api import NetDocuments


class RepositoryUserLog(AddonInput):
    def collect(self, account_details, proxy_settings, input_name, input_item, last_checkpoint):
        sourcetype = "netdocuments:repository:user:logs"

        netdocs_api = NetDocuments(self.logger, account_details)

        if not last_checkpoint:
            now = datetime.now()
            seven_days_ago = now - timedelta(days=1)  # update limit
            last_checkpoint = seven_days_ago.strftime("%Y-%m-%dT%H:%M:%SZ")

        repository_id = account_details.get('repository_id')
        response = netdocs_api.make_api_call(f'Repository/{repository_id}/log', params={"start_date": last_checkpoint, "Logtype": "consolidated", "format": "json"})

        self.logger.info("Completed the HTTP request to RepositoryUserLog.")

        if response:
            if response.status_code == 200:
                cleaned_response_text = response.text.lstrip('\ufeff')
                json_data = json.loads(cleaned_response_text)

                last_date = json_data[-1]['activity']['date']

                self.logger.info(f'Total events fetched from API {len(json_data)}')

                for i in range(len(json_data)-1, -1, -1):
                    if json_data[i]['activity']['date'] == last_date:
                        # pass   # ignoring the last date to avoid duplicate data
                        self.logger.debug(f"i={i} -> last_date")
                    else:
                        self.logger.debug(f"i={i} -> last_date not matching here breaking...")
                        break

                for j in range(0, i+1):
                    # self.logger.debug(f"i={i} -> ingesting line -> {json_data[j]}")
                    self.event_writer.write_event(
                        smi.Event(
                            data=json.dumps(json_data[j]['activity'], ensure_ascii=False, default=str),
                            index=input_item.get("index"),
                            sourcetype=sourcetype,
                        )
                    )

                self.logger.info(f'Ingested {i+1} events for input="{input_name.split("/")[-1]}" in the sourcetype="{sourcetype}"')
                return "{}Z".format(last_date)

            else:
                self.logger.error(f"Unable to fetch user data from repository={repository_id}, status_code={response.status_code}")
