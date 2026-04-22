import logging
import sys
from pathlib import Path

class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"

class ColoredFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.DEBUG: Colors.CYAN,
        logging.INFO: Colors.CYAN,
        logging.WARNING: Colors.YELLOW,
        logging.ERROR: Colors.RED,
        logging.CRITICAL: Colors.RED,
    }

    def format(self, record):
        color = self.LEVEL_COLORS.get(record.levelno, Colors.RESET)
        level = f"{color}{Colors.BOLD}{record.levelname}{Colors.RESET}"
        message = record.getMessage()
        return f"{level} - {message}"


def setup_logging(level=logging.INFO, log_file: Path | None = None):
    handlers = [logging.StreamHandler(sys.stdout)]
    handlers[0].setFormatter(ColoredFormatter())

    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        fh.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
        handlers.append(fh)

    logging.basicConfig(
        level=level,
        handlers=handlers,
        force=True
    )

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


def info(msg: str, *args, **kwargs):
    logging.getLogger("root").info(msg, *args, **kwargs)

def success(msg: str, *args, **kwargs):
    _logger = logging.getLogger("root")
    _logger.log(logging.INFO, f"{Colors.GREEN}{Colors.BOLD}SUCCESS{Colors.RESET} - {msg}", *args, **kwargs)

def warning(msg: str, *args, **kwargs):
    logging.getLogger("root").warning(msg, *args, **kwargs)

def error(msg: str, *args, **kwargs):
    logging.getLogger("root").error(msg, *args, **kwargs)
