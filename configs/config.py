import yaml


def get_config():
    with open("../configs/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config


cfg = get_config()