from brotherql_cli.appconfig import load_config

import typer
from rich import print

from zeroconf import Zeroconf, ServiceBrowser
import time

def __broad_search(timeout=5) -> str | None:
    printer = None

    model = load_config().get("model", None)
    if not model or model.strip() == "":
        model = "QL"

    class PrinterListener:
        def add_service(self, zeroconf:Zeroconf, type, name):
            info = zeroconf.get_service_info(type, name)
            if info and model in name:
                nonlocal printer
                printer = info.parsed_addresses()[0] if info.parsed_addresses() else None
        def update_service(self, zeroconf, type, name):
            # Mandatory but useless
            pass

    zeroconf = Zeroconf()
    listener = PrinterListener()
    browser = ServiceBrowser(zeroconf, "_ipp._tcp.local.", listener) # type: ignore
    time.sleep(timeout)
    zeroconf.close()
    return printer

def find_ip(informative:bool=False) -> str:
    attempts = load_config()["ATTEMPTS"]
    for i in range(attempts-1):
        if informative:
            print(f"[gold1 b][IP SCAN][/gold1 b] Searching for active printer, attempt [yellow b]{i+1}[/yellow b] of [magenta b]{attempts}[/magenta b]")
        ip = __broad_search()
        if ip:
            return ip
    raise Exception(f"Printer can't be found, [{attempts}] attempts have been made")

import os
import re

def ip_in_local_subnet(target_ip:str, attempts=4) -> bool:
    response = os.popen(f"ping -c {attempts} {target_ip}").read()
    recieved = re.findall(
        r"[0-4](?= packets received)",
        response,
        re.MULTILINE
    )
    if len(recieved) !=0 and int(recieved[0]) != 0:
        return True
    else:
        return False
        
__all__ = [
    "find_ip",
    "ip_in_local_subnet"
]