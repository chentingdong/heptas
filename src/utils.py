import os
from datetime import datetime
from ..configs.config import cfg


def now(format=None):
    if format is None:
        format = cfg["format"]["datetime_short"]

    now = datetime.utcnow().strftime(format)
    return now


def today(format=None):
    if format is None:
        format = cfg["format"]["date"]
    date = datetime.utcnow().strftime(format)
    return date