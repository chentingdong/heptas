import os
from datetime import datetime
from ..configs.config import cfg


def get_outfile_path(infile):
    dir = cfg["files"]["output_dir"]
    basename = os.path.basename(infile)
    file, ext = os.path.splitext(basename)
    timestamp = now()
    outfile_path = "{dir}/{file}.{timestamp}{ext}".format(**locals())
    return outfile_path


def now(format=None):
    if format is None:
        format = cfg["format"]["datetime_short"]

    now = datetime.utcnow().strftime(format)
    return now
