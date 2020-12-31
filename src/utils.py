import os
from datetime import datetime
from ..configs.config import cfg


def get_outfile_path(infile_path):
    dir = cfg["debug"]["output_dir"]
    basename = os.path.basename(infile_path)
    filename, ext = os.path.splitext(basename)
    timestamp = get_now()
    outfile_path = "{dir}/{filename}.{timestamp}{ext}".format(**locals())
    return outfile_path


def get_now(format=None):
    if format is None:
        format = cfg["format"]["datetime_short"]

    now = datetime.utcnow().strftime(format)
    return now
