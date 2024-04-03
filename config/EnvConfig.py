from dotenv import dotenv_values
import os

from enums.env_enum import Evn

def get_env_config():
    env = os.environ.get('env')
    config = {'env':env}
    if env == Evn.ENV_LOCAL.value:
        config.update(dotenv_values(".env_local"))
    return config