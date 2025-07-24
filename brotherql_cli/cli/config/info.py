from brotherql_cli.cli.config.definitions import ConfigField

from rich import print
from rich.table import Table
from rich.panel import Panel

import typer
app = typer.Typer()

@app.command(help="Explains what each config field is")
def info():
    table = Table(show_header=False, show_lines=True, show_edge=False)
    table.add_column(highlight=True, no_wrap=True, justify="right", vertical="middle", style="yellow b")
    table.add_column(justify="left", vertical="middle", style="magenta")
    for c in ConfigField:
        table.add_row(c.value, c.desc)
    
    print(Panel.fit(table, title="[salmon1]CONFIG OPTIONS[/salmon1]", style="salmon1"))