import click
from typer.core import TyperGroup

from tabulate import tabulate
from typing import Any

class PrintException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

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
    
from brotherql_cli.logging import log_exception
class ErrorHandlerTyper(TyperGroup):
    def invoke(self, ctx:click.Context) -> Any:
        try:
            return super().invoke(ctx)
        except Exception as e:\
            # Walk to the last traceback frame
            tb = e.__traceback__
            while tb.tb_next: # type: ignore
                tb = tb.tb_next # type: ignore
            frame = tb.tb_frame # type: ignore

            # Extract file, locals, full traceback
            filename = frame.f_code.co_filename
            locals = {k: v for k, v in frame.f_locals.items()
                        if not k.startswith('__')}
            
            exception = CLIError(filename, locals, e)
            log_exception(exception)
            raise exception