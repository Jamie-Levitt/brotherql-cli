import os
import yaml

from brotherql_cli.definitions import ROOT_DIR, ConfigSchema

CONF_PATH = ROOT_DIR / "config.yaml"

def affirm_configfile():
    if not os.path.exists(CONF_PATH) or not os.path.isfile(CONF_PATH):
        with open(CONF_PATH, "w") as f:
            yaml.dump(ConfigSchema(model="QL-820NWB", ip=""), f, default_flow_style=False)

def load_config() -> ConfigSchema:
    affirm_configfile()
    with open(CONF_PATH, "r") as f:
        config = yaml.safe_load(f)
    return ConfigSchema(config)

def set_config(model:str|None=None, ip:str|None=None):
    affirm_configfile()
    config = load_config()
    if model: config['model'] = model
    if ip: config['ip'] = ip
    with open(CONF_PATH, "w") as f:
        yaml.dump(config, f, default_flow_style=False)
    return config