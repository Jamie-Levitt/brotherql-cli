from brotherql_cli.cli.config.definitions import ConfigField, autocomplete_config_field
from brotherql_cli.appconfig import load_config, set_config

from rich import print
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.panel import Panel

import typer
app = typer.Typer()

from typing import Annotated

@app.command(help="Sets the value of a given config field")
def set(
    field: Annotated[
        ConfigField, typer.Argument(help="The saved config value to be displayed",
                          autocompletion=autocomplete_config_field)
        ]
    ):
    current_val = load_config()[field.value]
    print(f"Current [yellow b]{field.value}[/yellow b]: {'"'*(field.vartype is str)}[magenta]{current_val}[/magenta]{'"'*(field.vartype is str)}")
    typer.confirm("Are you sure you want to change it?", abort=True)
    print(field.defin)
    success = False
    while not success:
        new_val = Prompt.ask(f"New [yellow b]{field.value}[/yellow b]")
        new_val = field.vartype(new_val)
        if not field.validator(new_val):
            print("[dark_orange3 b]INVALID VALUE[/dark_orange3 b]")
            print(field.defin)
            typer.confirm("Retry?", abort=True)
        else:
            table = Table(show_lines=True, show_edge=False)
            table.add_column(header=f"[yellow b]OLD {field.value}[/yellow b]",
                             no_wrap=True, justify="center", vertical="middle",
                             ratio=1, style="magenta")
            table.add_column(header=f"[yellow b]NEW {field.value}[/yellow b]",
                             no_wrap=True, justify="center", vertical="middle",
                             ratio=1, style="magenta")
            table.add_row(f"{'"'*(field.vartype is str)}{current_val}{'"'*(field.vartype is str)}", f"{'"'*(field.vartype is str)}{new_val}{'"'*(field.vartype is str)}")
            print(Panel.fit(table, title="[salmon1]CONFIG VALUES[/salmon1]", style="salmon1"))
            conf = Confirm.ask(f"Are you sure you want to change [yellow b]{field.value}[/yellow b]")
            if not conf: raise typer.Abort()
            success = True

    try:
        set_config(field.value, new_val)
        print(f"[yellow b]{field.value} has been set to [magenta]{new_val}[/magenta]")
    except Exception as e:
        print(f"[red b]AN ERROR HAS OCCURED[/red b]")
        typer.confirm("Print exception (needed for debugging)?")
        raise e