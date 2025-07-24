import typer

from brotherql_cli.cli.config.info import app as info_app
from brotherql_cli.cli.config.read import app as read_app
from brotherql_cli.cli.config.set import app as set_app
from brotherql_cli.cli.config.refresh import app as refresh_app

config_app = typer.Typer()
config_app.add_typer(info_app)
config_app.add_typer(read_app)
config_app.add_typer(set_app)
config_app.add_typer(refresh_app)

@config_app.callback()
def config_callback():
    """
    Config tools for brotherql-cli
    """

__all__ = [
    "config_app"
]