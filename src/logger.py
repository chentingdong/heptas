import logging
from ..configs.config import cfg

def get_logger(name=None):
    if name is None:
        name = __name__

    formatter = logging.Formatter(cfg["debug"]["logging_format"])
    log_path = "{dir}/{name}.log".format(dir=cfg["debug"]["log_dir"], name=name)
    fh = logging.FileHandler(log_path)
    fh.setFormatter(formatter)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.root.setLevel(cfg["debug"]["level"])
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


translation_logger = get_logger("translation")
reporting_logger = get_logger("reporting")