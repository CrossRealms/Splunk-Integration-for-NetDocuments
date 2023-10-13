import json
import logging
import sys
import traceback

import import_declare_test
from package.bin.input_checkpointer import NetDocumentsInputCheckpointer
from solnlib import conf_manager, log
from splunklib import modularinput as smi

from netdocuments_api import NetDocuments
from utils import ADDON_NAME


def logger_for_input(input_name: str) -> logging.Logger:
    return log.Logs().get_logger(f"{ADDON_NAME.lower()}_{input_name}")


def get_account_details(session_key: str, account_name: str):
    cfm = conf_manager.ConfManager(
        session_key,
        ADDON_NAME,
        realm=f"__REST_CREDENTIAL__#{ADDON_NAME}#configs/conf-TA_NetDocuments_account",
    )
    account_conf_file = cfm.get_conf("TA_NetDocuments_account")
    return {
        "client_id": account_conf_file.get(account_name).get('client_id'),
        "client_secret": account_conf_file.get(account_name).get('client_secret'),
        "access_token": account_conf_file.get(account_name).get('access_token'),
        "refresh_token": account_conf_file.get(account_name).get('refresh_token')
    }


class Input(smi.Script):
    def __init__(self):
        super().__init__()

    def get_scheme(self):
        scheme = smi.Scheme("repository_user_logs")
        scheme.description = "repository_user_logs input"
        scheme.use_external_validation = True
        scheme.streaming_mode_xml = True
        scheme.use_single_instance = False
        scheme.add_argument(
            smi.Argument(
                "name", title="Name", description="Name", required_on_create=True
            )
        )
        return scheme

    def validate_input(self, definition: smi.ValidationDefinition):
        return

    def stream_events(self, inputs: smi.InputDefinition, event_writer: smi.EventWriter):
        # inputs.inputs is a Python dictionary object like:
        # {
        #   "repository_user_logs://<input_name>": {
        #     "account": "<account_name>",
        #     "disabled": "0",
        #     "host": "$decideOnStartup",
        #     "index": "<index_name>",
        #     "interval": "<interval_value>",
        #     "python.version": "python3",
        #   },
        # }

        # TODO - Need to delete checkpoints for input which got deleted

        for input_name, input_item in inputs.inputs.items():
            normalized_input_name = input_name.split("/")[-1]
            logger = logger_for_input(normalized_input_name)
            try:
                session_key = self._input_definition.metadata["session_key"]
                log_level = conf_manager.get_log_level(
                    logger=logger,
                    session_key=session_key,
                    app_name=ADDON_NAME,
                    conf_name=f"{ADDON_NAME}_settings",
                )
                logger.setLevel(log_level)
                log.modular_input_start(logger, normalized_input_name)

                account_name = input_item.get('account_name')
                account_details = get_account_details(session_key, account_name)
                # proxy_settings = get_proxy_settings(session_key, logger)
                client_id = account_details.get('client_id')
                client_secret = account_details.get('client_secret')
                access_token = account_details.get('access_token')
                refresh_token = account_details.get('refresh_token')

                # data = get_data_from_api(logger, api_key)
                netdocs_api = NetDocuments(logger, client_id=client_id, client_secret=client_secret, access_token=access_token, refresh_token=refresh_token)

                checkpointer = NetDocumentsInputCheckpointer(session_key, logger, normalized_input_name)
                start_date = checkpointer.get()   # format supported yyyy-MM-ddThh:mm:ssZ

                repository_id = input_item.get('repository_id')
                response = netdocs_api.make_api_call(f'/v1/Repository/{repository_id}/log', params={"start_date": start_date, "Logtype": "consolidated", "format": "json"})

                if response.status_code == 200:
                    sourcetype = "netdocuments:repository:user:logs"

                    res_json = response.json()
                    for line in res_json:
                        event_writer.write_event(
                            smi.Event(
                                data=json.dumps(line, ensure_ascii=False, default=str),
                                index=input_item.get("index"),
                                sourcetype=sourcetype,
                            )
                        )
                    checkpointer.update("new_val")   # TODO - update proper checkpoint value, format supported yyyy-MM-ddThh:mm:ssZ
                    log.events_ingested(
                        logger, normalized_input_name, sourcetype, len(res_json)
                    )
                else:
                    logger.error(f"Unable to fetch user data from repository={repository_id}, status_code={response.status_code}")

                log.modular_input_end(logger, normalized_input_name)
            except Exception as e:
                logger.error(
                    f"Exception raised while ingesting data for "
                    f"repository_user_logs: {e}. Traceback: "
                    f"{traceback.format_exc()}"
                )


if __name__ == "__main__":
    exit_code = Input().run(sys.argv)
    sys.exit(exit_code)
