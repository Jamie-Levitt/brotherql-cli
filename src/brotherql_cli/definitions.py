import os
import pathlib

ROOT_DIR = pathlib.Path(os.path.abspath(__file__)).parent

from typing import TypedDict

class ConfigSchema(TypedDict):
    ip: str
    model: str
    search_attempts: int

import click
from tabulate import tabulate

class CLIError(click.ClickException):
    def __init__(self, filename:str, locals:dict, exception:Exception) -> None:
        super().__init__(f"{filename}\n\n"
                         f"{exception.__class__.__name__}: {exception}\n\n"
                         f"Variables:\n{CLIError.tabulate_relevant_vars(locals)}")
        
    @classmethod
    def tabulate_relevant_vars(cls, relevant_vars:dict) -> str:
        vars = relevant_vars.keys()
        vals = relevant_vars.values()
        return tabulate({"VARIABLE": vars, "VALUE": vals})