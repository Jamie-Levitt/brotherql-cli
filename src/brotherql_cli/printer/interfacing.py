from brotherql_cli.config import load_config
from brotherql_cli.printer.searching import broad_search
from brotherql_cli.label import generate_image

import time

from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from brother_ql.raster import BrotherQLRaster

def print_from_lines(label_lines:list[str]):
    backend = 'network'
    for i in range(2):
        printer_ip = broad_search()
        if printer_ip: break
        if i == 2: raise Exception("Printer can't be found")
        time.sleep(2)

    image = generate_image(label_lines)
    qlr = BrotherQLRaster(load_config()["model"])

    instructions = convert(
        qlr=qlr, 
        images=[image],  # Takes a list of file names or PIL objects.
        label='62', 
        rotate='0',  # 'Auto', '0', '90', '270'
        threshold=70.0,  # Black and white threshold in percent.
        dither=False, 
        compress=False, 
        dpi_600=False, 
        red=True,
        hq=True,  # False for low quality.
        cut=True
    )  

    send(instructions=instructions, printer_identifier=printer_ip, backend_identifier=backend, blocking=True)
