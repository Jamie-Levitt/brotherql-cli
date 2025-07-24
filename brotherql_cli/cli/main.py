import typer
from brotherql_cli.cli.exceptionhandle import ErrorHandlerTyper
app = typer.Typer(cls=ErrorHandlerTyper,pretty_exceptions_enable=False)

from brotherql_cli.cli.config import config_app
app.add_typer(config_app, name="config")

from brotherql_cli.cli.print import print_app
app.add_typer(print_app)

@app.callback()
def callback():
    """
    brotherql-cli for printing labels with Brother QL label printer
    """

__all__ = [
    "app"
]