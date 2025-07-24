from brotherql_cli.cli.config.definitions import autocomplete_config_field
from brotherql_cli.appconfig import load_config

from rich import print
from rich.table import Table
from rich.panel import Panel

import typer
app = typer.Typer()

from typing_extensions import Annotated

@app.command(help="Shows the cli's stored config")
def read():
    config = load_config()
    disp = Table(show_header=False, show_lines=True, show_edge=False)
    disp.add_column(highlight=True, no_wrap=True, justify="right", vertical="middle", style="yellow b")
    disp.add_column(justify="left", vertical="middle", style="magenta")

    for c, v in config.items():
        if type(v) == str:
            v = f'"{v}"'
        disp.add_row(c, str(v))

    print(Panel.fit(disp, title="[salmon1]SAVED CONFIG[/salmon1]", style="salmon1"))