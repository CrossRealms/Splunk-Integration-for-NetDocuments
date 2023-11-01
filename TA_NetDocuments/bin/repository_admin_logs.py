
import sys

import import_declare_test
from splunklib import modularinput as smi
from input_repository_admin_logs import RepositoryAdminLog



class Input(smi.Script):
    def __init__(self):
        super().__init__()

    def get_scheme(self):
        scheme = smi.Scheme("repository_admin_logs")
        scheme.description = "repository_admin_logs input"
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
        session_key = self._input_definition.metadata["session_key"]

        for input_name, input_item in inputs.inputs.items():
            RepositoryAdminLog(session_key, input_name, input_item, event_writer)


if __name__ == "__main__":
    exit_code = Input().run(sys.argv)
    sys.exit(exit_code)
