import typer

app = typer.Typer(no_args_is_help=True, invoke_without_command=True)

from brotherql_cli.cli.config import config_app
app.add_typer(config_app, name="config")

from brotherql_cli.cli.print import print_app
app.add_typer(print_app)

@config_app.callback(invoke_without_command=True)
def default(ctx: typer.Context):
    """
    brotherql-cli for printing labels with Brother QL label printer
    """
    typer.echo(ctx.get_help())

__all__ = [
    "app"
]