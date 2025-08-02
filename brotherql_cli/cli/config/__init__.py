import typer

from brotherql_cli.cli.config.info import app as info_app
from brotherql_cli.cli.config.read import app as read_app
from brotherql_cli.cli.config.set import app as set_app
from brotherql_cli.cli.config.refresh import app as refresh_app

config_app = typer.Typer(no_args_is_help=True)
config_app.add_typer(info_app)
config_app.add_typer(read_app)
config_app.add_typer(set_app)
config_app.add_typer(refresh_app)

@config_app.callback(invoke_without_command=True)
def default(ctx: typer.Context):
    """
    Config tools for brotherql-cli
    """
    typer.echo(ctx.get_help())

__all__ = [
    "config_app"
]