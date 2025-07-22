from zeroconf import Zeroconf, ServiceBrowser
import time

from brotherql_cli.config import load_config

def broad_search(timeout=5) -> str | None:
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

__all__ = [
    "broad_search"
]