import os
import pathlib

ROOT_DIR = pathlib.Path(os.path.abspath(__file__)).parent

from typing import TypedDict

class ConfigSchema(TypedDict):
    model: str
    ip: str

class PrinterNotFoundError(Exception):
    def __init__(self, message:str) -> None:
        super().__init__(message)