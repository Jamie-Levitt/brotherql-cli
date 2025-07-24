from brotherql_cli.appconfig import load_config, set_config
from brotherql_cli.printer.searching import find_ip, ip_in_local_subnet

from rich import print
from rich.table import Table
from rich.panel import Panel

import typer
app = typer.Typer()

@app.command()
def refresh():
    """
    Automatically find active printer's IP Adress
    """
    current_ip = load_config()["IP"]
    print(f'Current IP: "[magenta b]{current_ip}[/magenta b]"')
    if current_ip and current_ip != "" and ip_in_local_subnet(current_ip):
        typer.confirm("Printer IP is active in network, are you sure you want to scan?", abort=True)
    
    try:
        new_ip = find_ip(informative=True)
        if new_ip == current_ip:
            print(f'Stored IP "[magenta b]{current_ip}[/magenta b]" still active, please manually change IP if innacurate')
            raise typer.Exit()
        print(f"[gold1 b][IP SCAN][/gold1 b] Found active printer IP")
        table = Table(show_lines=True, show_edge=False)
        table.add_column(header=f"[yellow b]STORED IP[/yellow b]",
                            no_wrap=True, justify="center", vertical="middle",
                            ratio=1, style="magenta")
        table.add_column(header=f"[yellow b]FOUND IP[/yellow b]",
                            no_wrap=True, justify="center", vertical="middle",
                            ratio=1, style="magenta")
        table.add_row(f'"{current_ip}"', f'"{new_ip}"')
        print(Panel.fit(table, title="[salmon1]CONFIG VALUES[/salmon1]", style="salmon1"))
        typer.confirm("Do you want to replace stored IP with found IP?", abort=True)
        ref = set_config("IP", new_ip)
        print(f'IP succesfully set to "[magenta b]{ref["IP"]}[/magenta b]"')
    except typer.Exit or typer.Abort as e:
        raise e
    except:
        print(f"[gold1 b][IP SCAN][/gold1 b] [red1 b]Failed to find active IP[/red1 b]")
        raise typer.Exit()