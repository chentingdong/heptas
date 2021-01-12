import os, yaml
from datetime import datetime


def get_config():
    with open("../configs/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config

cfg = get_config()

def get_infile_path(infile):
    return "{dir}/{file}".format(dir=cfg["files"]["input_dir"], file=infile)


def get_outfile_path(
    infile, engine=None, targetLanguageCode=cfg["translate"]["targetLanguageCode"]
):
    cfg = get_config()
    if engine is None:
        engine = cfg["translate"]["engine"]

    dir = cfg["files"]["output_dir"]
    basename = os.path.basename(infile)
    outfile_path = "{dir}/{targetLanguageCode}.{basename}".format(**locals())
    return outfile_path


def get_report_path(filename):
    dir = cfg["files"]["report_dir"]
    reportfile_path = "{dir}/report.{filename}.csv".format(**locals())
    return reportfile_path

