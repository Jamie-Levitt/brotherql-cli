from brotherql_cli.config import load_config
from brotherql_cli.label import generate_image, BrotherQLRaster, convert

from brotherql_cli.printer.searching import broad_search
from brotherql_cli.printer.backends.helpers import send
from brotherql_cli.definitions import PrinterNotFoundError

def print_from_lines(label_lines: list[str]):
    printer_ip = affirm_printer()
    if not printer_ip:
        raise PrinterNotFoundError(
            f"No active printer of model [{load_config()['model']}] can be found on the network"
        )

    image = generate_image(label_lines)
    raster = BrotherQLRaster()
    instructions = convert(raster, [image])

    send(instructions, printer_ip)

def affirm_printer() -> str | None:
    return broad_search()

__all__ = [
    "print_from_lines",
    "affirm_printer"
]