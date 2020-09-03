"""Create custom logger."""
from sys import stdout
from loguru import logger as loguru_logger


def create_logger():
    """Create custom logger."""
    loguru_logger.remove()
    loguru_logger.add(
        stdout,
        colorize=True,
        level="INFO",
        catch=True,
        format="<green>{time:MM-DD-YYYY HH:mm:ss}</green>"
               + "<light-red> | </light-red>"
               + "<white>{message}</white>"
    )
    return loguru_logger


logger = create_logger()
