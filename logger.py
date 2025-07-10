from datetime import datetime, timezone
import logging

def init():
    """
    Initialize the application logger.
    """
    logging.Formatter.formatTime = format_time
    logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(asctime)s: %(message)s")

def format_time(self, record, datefmt=None):
    """
    Return the date/time formatted according to ISO.
    """
    return datetime.fromtimestamp(record.created, timezone.utc).astimezone().isoformat(timespec="milliseconds")