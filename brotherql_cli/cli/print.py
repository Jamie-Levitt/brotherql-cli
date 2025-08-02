from brotherql_cli.cli.exceptionhandle import ErrorHandlerTyper, PrintException
from brotherql_cli.printer import print_from_lines

import typer
print_app = typer.Typer(cls=ErrorHandlerTyper, pretty_exceptions_enable=False)

@print_app.command("print", help="Print list of strings to label")
def print_label(label_lines:str):
    try:
        # print("[DEBUG] Cleaning lines")
        lines = [line.strip() for line in label_lines.split(";")
                    if line.strip() != ""]
        if len(lines) == 0:
            raise ValueError(f"Argument label_lines cannot be empty, or full of empty strings. [{label_lines}]")
    
        # print("[DEBUG] Sending to print")
        print_from_lines(lines)
    except Exception as e:
        raise PrintException(e)