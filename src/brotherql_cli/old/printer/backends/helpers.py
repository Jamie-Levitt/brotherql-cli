from brotherql_cli.printer.backends import backend_factory

import time

def send(instructions, printer_identifier:str):
    """
    Send instruction bytes to a printer.

    :param bytes instructions: The instructions to be sent to the printer.
    :param str printer_identifier: Identifier for the printer.
    :param str backend_identifier: Can enforce the use of a specific backend.
    :param bool blocking: Indicates whether the function call should block while waiting for the completion of the printing.
    """

    status = {
      'instructions_sent': True, # The instructions were sent to the printer.
      'outcome': 'unknown', # String description of the outcome of the sending operation like: 'unknown', 'sent', 'printed', 'error'
      'printer_state': None, # If the selected backend supports reading back the printer state, this key will contain it.
      'did_print': False, # If True, a print was produced. It defaults to False if the outcome is uncertain (due to a backend without read-back capability).
      'ready_for_next_job': False, # If True, the printer is ready to receive the next instructions. It defaults to False if the state is unknown.
    }
    be = backend_factory()
    BrotherQLBackend = be

    printer = BrotherQLBackend(printer_identifier)

    start = time.time()
    printer.write(instructions)
    status['outcome'] = 'sent'

    return status