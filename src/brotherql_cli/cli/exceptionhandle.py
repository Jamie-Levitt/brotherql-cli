from typer.core import TyperGroup
import click
import traceback

from typing import Any
from brotherql_cli.definitions import CLIError

class ErrorHandlerTyper(TyperGroup):
    def invoke(self, ctx: click.Context) -> Any:
        try:
            return super().invoke(ctx)
        except Exception as e:
            # Walk to the last traceback frame
            tb = e.__traceback__
            while tb.tb_next:
                tb = tb.tb_next
            frame = tb.tb_frame

            # Extract file, locals, full traceback
            filename = frame.f_code.co_filename
            locals = {k: v 
                            for k, v in frame.f_locals.items()
                                if not k.startswith('__')}
            
            raise CLIError(filename, locals, e)