import typer
from typing import List

from brotherql_cli.cli.exceptionhandle import ErrorHandlerTyper
from brotherql_cli.cli.config import config_app

app = typer.Typer(cls=ErrorHandlerTyper, pretty_exceptions_enable=False)
app.add_typer(config_app, name="config")

from brotherql_cli.printer import print_from_lines 

@app.command("print")
def print_label(label_lines:List[str]):
    print("[DEBUG] Cleaning lines")
    label_lines = [line.strip() for line in label_lines
                    if line.strip() != ""]
    if len(label_lines) == 0:
        raise ValueError(f"Argument label_lines cannot be empty, or full of empty strings. [{label_lines}]")
    
    print("[DEBUG] Sending to print")
    print_from_lines(label_lines)

__all__ = [
    "app"
]