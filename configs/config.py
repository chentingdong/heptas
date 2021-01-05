import os, yaml
from datetime import datetime


def get_config():
    with open("../configs/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config


def get_outfile_path(infile, engine=None):
    cfg = get_config()
    if engine is None:
        engine = cfg["translate"]["engine"]

    dir = cfg["files"]["output_dir"]
    basename = os.path.basename(infile)
    format = cfg["format"]["datetime_file"]
    timestamp = datetime.utcnow().strftime(format)
    outfile_path = "{dir}/{timestamp}.{engine}.{basename}".format(**locals())
    return outfile_path


cfg = get_config()
