from pathlib import Path
import typer

APP_NAME = "brotherql-cli"

LOG_DIR:Path = Path(typer.get_app_dir(APP_NAME)) / "logs"

from brotherql_cli.cli.exceptionhandle import PrintException
def __affirm_log_dir() -> None:
    if not LOG_DIR.exists():
        try:
            LOG_DIR.mkdir()
        except Exception as e:
            raise PrintException(e)

from datetime import datetime
def log_exception(exception:Exception) -> None:
    __affirm_log_dir()
    path = LOG_DIR/f"[{datetime.now().strftime("%S_%M_%H %d_%m_%Y")}]{exception.__class__.__name__}.txt"
    with open(path.absolute(), "w") as f:
        f.write(f"{datetime.now()}\n{exception}")

        