from zeroconf import Zeroconf, ServiceBrowser
import time

from brotherql_cli.config import load_config

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

def find_ip() -> str:
    attempts = load_config()["search_attempts"]
    for i in range(attempts):
        print(f"[DEBUG] Scanning for active printer IP, attempt [{i}] of [{attempts}]")
        ip = __broad_search()
        if ip:
            print(f"[DEBUG] Active printer IP found")
            return ip
    raise Exception(f"Printer can't be found, [{attempts}] attempts have been made")

import socket
import ipaddress

def ip_in_local_subnet(target_ip:str) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_network_address = s.getsockname()[0]
    s.close()

    return ipaddress.ip_address(target_ip) in ipaddress.ip_network(local_network_address)

__all__ = [
    "find_ip",
    "ip_in_local_subnet"
]