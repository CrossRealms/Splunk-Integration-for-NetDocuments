
import sys
import logging
import traceback

import import_declare_test

from solnlib.modular_input import checkpointer
from solnlib import conf_manager
from splunktaucclib.rest_handler.admin_external import AdminExternalHandler

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

    def update(self, new_val):
        try:
            ck = checkpointer.KVStoreCheckpointer(
                self.input_name, self.session_key, ADDON_NAME)
            return ck.update(self.input_name, new_val)
        except Exception as exception:
            self.logger.exception("Error occurred while updating the checkpoint, error={}".format(exception))

    def delete(self):
        try:
            ck = checkpointer.KVStoreCheckpointer(
                self.input_name, self.session_key, ADDON_NAME)
            return ck.delete(self.input_name)
        except Exception as exception:
            self.logger.exception("Error occurred while deleting the checkpoint, error={}".format(exception))



def get_account_details(session_key: str, logger, account_name: str):
    cfm = conf_manager.ConfManager(
        session_key,
        ADDON_NAME,
        realm=f"__REST_CREDENTIAL__#{ADDON_NAME}#configs/conf-{NORMALIZED_ADDON_NAME}_account",
    )
    account_conf_file = cfm.get_conf(f"{NORMALIZED_ADDON_NAME}_account")
    return account_conf_file.get(account_name)


def get_log_level(session_key: str):
    log_level = logging.INFO
    try:
        # TODO - this does not work as expected.
        log_level = conf_manager.get_log_level(
            session_key=session_key,
            app_name=ADDON_NAME,
            conf_name=f"{NORMALIZED_ADDON_NAME}_settings",
        )
    except:
        pass
    return log_level



class AddonInput:
    def __init__(self, session_key, input_name, input_item, event_writer) -> None:
        normalized_input_name = input_name.split("/")[-1]

        self.session_key = session_key
        self.event_writer = event_writer

        log_level = get_log_level(self.session_key)
        log_level = logging.DEBUG   # TODO - something to be removed
        self.logger = logger_manager.setup_logging(normalized_input_name, log_level)

        try:
            self.logger.info(f'Modular input "{normalized_input_name}" started.')

            self.logger.debug(f"input_name={input_name}, input_item={input_item}")

            account_name = input_item.get('account')
            account_details = get_account_details(session_key, self.logger, account_name)
            # proxy_settings = get_proxy_settings(session_key, logger)

            input_checkpointer = AddonInputCheckpointer(session_key, self.logger, normalized_input_name)
            last_checkpoint = input_checkpointer.get()
            self.logger.info(f"input={normalized_input_name} -> last_checkpoint={last_checkpoint}")

            self.logger.debug("before self.collect()")
            updated_checkpoint = self.collect(account_details, proxy_settings=None, input_name=input_name, input_item=input_item, last_checkpoint=last_checkpoint)
            self.logger.debug("after self.collect()")
            self.logger.debug(f"input={normalized_input_name} -> updating the checkpoint to {updated_checkpoint}")
            if updated_checkpoint:
                input_checkpointer.update(updated_checkpoint)

            self.logger.info(f'Modular input "{normalized_input_name}" ended.')

        except Exception as e:
            self.logger.error(
                f'Exception raised while ingesting data for input="{normalized_input_name}" {e}. Traceback: {traceback.format_exc()}'
            )


    def collect(self, account_details, proxy_settings, input_name, input_item, last_checkpoint):
        self.logger.error("This collect() function should not be called.")
        raise Exception("collect method has not been implemented.")



class InputHelperRestHandler(AdminExternalHandler):
    def __init__(self, *args, **kwargs):
        AdminExternalHandler.__init__(self, *args, **kwargs)

    def handleList(self, confInfo):
        AdminExternalHandler.handleList(self, confInfo)

    def handleEdit(self, confInfo):
        AdminExternalHandler.handleEdit(self, confInfo)

    def handleCreate(self, confInfo):
        AdminExternalHandler.handleCreate(self, confInfo)

    def handleRemove(self, confInfo):
        # Deleting the checkpoint to avoid issue when user tries to delete the input but then tries to recreate the input with the same name

        session_key = self.getSessionKey()
        log_level = get_log_level(session_key)
        input_name = self.callerArgs.id
        if input_name:
            logger = logger_manager.setup_logging(input_name, log_level)

            input_checkpointer = AddonInputCheckpointer(self.getSessionKey(), logger, input_name)
            last_checkpoint = input_checkpointer.get()

            if last_checkpoint:
                logger.info(f"Deleting the checkpoint for input={input_name} with last found checkpoint was {last_checkpoint}")
                input_checkpointer.delete()
                logger.info(f"Deleted the input checkpoint for input={input_name}")
            else:
                logger.info(f"No checkpoint present for input={input_name}")

            AdminExternalHandler.handleRemove(self, confInfo)

        else:
            logger = logger_manager.setup_logging("delete_input_error", log_level)
            err_msg = "Unable to find the input name in the handler."
            logger.error(err_msg)
            raise Exception(err_msg)
