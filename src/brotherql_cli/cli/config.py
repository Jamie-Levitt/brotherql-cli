import typer

from brotherql_cli.config import load_config, set_config

config_app = typer.Typer()

model_option_app = typer.Typer()
# ip_option_app = typer.Typer()

config_app.add_typer(model_option_app, name="model")
# config_app.add_typer(ip_option_app, name="ip")

@model_option_app.command("read")
def config_model_read():
    """
    Read current printer model from configuration
    """
    config = load_config()
    typer.echo(f"Model: {config['model']}")

@model_option_app.command("set")
def config_model_set(model: str):
    """
    Set printer model in configuration
    """
    if not model or model.strip() == "":
        typer.echo("Model cannot be empty.")
        raise typer.Exit(code=1)
    set_config(model=model)
    typer.echo(f"Configuration updated successfully, model set to [{model}].")

# @ip_option_app.command("read")
# def config_ip_read():
#     """
#     Read current printer IP Address from configuration
#     """
#     ip = load_config()["ip"]
#     if not ip or ip.strip() == "":
#         typer.echo("No IP address configured.")
#         raise typer.Exit(code=1)
#     typer.echo(f"IP Address: {ip}")

# @ip_option_app.command("set")
# def config_ip_set(ip: str):
#     """
#     Manually set printer IP Address in configuration
#     """
#     if not ip or ip.strip() == "":
#         typer.echo("IP Address cannot be empty.")
#         raise typer.Exit(code=1)
#     set_config(ip=ip)
#     typer.echo(f"Configuration updated successfully, IP Address set to [{ip}].")

# from brotherql_cli.printer import affirm_printer

# @ip_option_app.command("scan")
# def config_ip_scan():
#     """
#     Automatically find and update IP of active Brother QL printer
#     """
#     config = load_config()
#     current = config["ip"]
#     typer.echo(f"Current stored IP Address is [{current}]")
#     scan = typer.confirm("Are you sure you want to scan for a new one?")
#     if scan:
#         new = affirm_printer()
#         if new:
#             if new == current:
#                 typer.echo(f"Found IP Address [{new}] is identical to stored, no change has been made")
#             else:
#                 typer.echo(f"Replaced stored IP Address [{current}] with found IP Address [{new}]")
#         else:
#             typer.echo(f"No active printer of model [{config["model"]}] can be found on the network")


__all__ = [
    "config_app"
]