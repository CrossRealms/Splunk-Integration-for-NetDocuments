
import sys
import logging
import traceback
from solnlib.modular_input import checkpointer
from solnlib import conf_manager

from addon_name import ADDON_NAME, NORMALIZED_ADDON_NAME
import logger_manager


class AddonInputCheckpointer:
    def __init__(self, session_key, logger, input_name) -> None:
        self.session_key = session_key
        self.logger = logger
        self.input_name = input_name

    def get(self):
        try:
            ck = checkpointer.KVStoreCheckpointer(
                self.input_name, self.session_key, ADDON_NAME)
            return ck.get(self.input_name)
        except Exception as exception:
            self.logger.error("Error occurred while fetching checkpoint, error={}".format(exception))
            sys.exit(1)

    def update(self, new_val):
        try:
            ck = checkpointer.KVStoreCheckpointer(
                self.input_name, self.session_key, ADDON_NAME)
            return ck.update(self.input_name, new_val)
        except Exception as exception:
            self.logger.error("Error occurred while updating the checkpoint, error={}".format(exception))
            sys.exit(1)

    def delete(self):
        try:
            ck = checkpointer.KVStoreCheckpointer(
                self.input_name, self.session_key, ADDON_NAME)
            return ck.delete(self.input_name)
        except Exception as exception:
            self.logger.error("Error occurred while deleting the checkpoint, error={}".format(exception))
            sys.exit(1)



def get_account_details(session_key: str, logger, account_name: str):
    cfm = conf_manager.ConfManager(
        session_key,
        ADDON_NAME,
        realm=f"__REST_CREDENTIAL__#{ADDON_NAME}#configs/conf-{NORMALIZED_ADDON_NAME}_account",
    )
    account_conf_file = cfm.get_conf(f"{NORMALIZED_ADDON_NAME}_account")
    return account_conf_file.get(account_name)



class AddonInput:
    def __init__(self, session_key, input_name, input_item, event_writer) -> None:
        normalized_input_name = input_name.split("/")[-1]

        self.session_key = session_key
        self.event_writer = event_writer
        
        log_level = logging.INFO
        try:
            log_level = conf_manager.get_log_level(
                session_key=session_key,
                app_name=ADDON_NAME,
                conf_name=f"{NORMALIZED_ADDON_NAME}_settings",
            )
        except:
            pass

        self.logger = logger_manager.setup_logging(normalized_input_name, log_level)

        try:
            self.logger.info(f'Modular input "{normalized_input_name}" started.')

            self.logger.info(f"input_name={input_name}, input_item={input_item}")

            account_name = input_item.get('account')
            account_details = get_account_details(session_key, self.logger, account_name)
            # proxy_settings = get_proxy_settings(session_key, logger)

            checkpointer = AddonInputCheckpointer(session_key, self.logger, normalized_input_name)
            last_checkpoint = checkpointer.get()

            updated_checkpoint = self.collect(account_details, proxy_settings=None, input_name=input_name, input_item=input_item, last_checkpoint=last_checkpoint)
            checkpointer.update(updated_checkpoint)

            self.logger.info(f'Modular input "{normalized_input_name}" ended.')

        except Exception as e:
            self.logger.error(
                f'Exception raised while ingesting data for input="{normalized_input_name}" {e}. Traceback: {traceback.format_exc()}'
            )


    def collect(self, account_details, proxy_settings, input_name, input_item, last_checkpoint):
        raise Exception("collect method has not been implemented.")



