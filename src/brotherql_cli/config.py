import os
import yaml

from brotherql_cli.definitions import ROOT_DIR, ConfigSchema

CONF_PATH = ROOT_DIR / "config.yaml"

def __gen_new_config() -> None:
    with open(CONF_PATH, "w") as f:
        yaml.dump(ConfigSchema(ip="", model="QL-820NWB", search_attempts=4), f, default_flow_style=False)

def affirm_configfile() -> None:
    if not os.path.exists(CONF_PATH) or not os.path.isfile(CONF_PATH):
        __gen_new_config()

def load_config() -> ConfigSchema:
    affirm_configfile()
    with open(CONF_PATH, "r") as f:
        config = yaml.safe_load(f)
    try:
        return ConfigSchema(config)
    except:
        __gen_new_config()
        return ConfigSchema(ip="", model="QL-820NWB", search_attempts=4)

def set_config(ip:str|None=None, model:str|None=None, search_attempts:int|None=None) -> ConfigSchema:
    affirm_configfile()
    config = load_config()
    if ip: config["ip"] = ip
    if model: config["model"] = model
    if search_attempts: config["search_attempts"] = search_attempts
    with open(CONF_PATH, "w") as f:
        yaml.dump(config, f, default_flow_style=False)
    return config