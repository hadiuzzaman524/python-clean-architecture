
from config.config_model import AppConfig
import tomli
from pathlib import Path
import os


class ConfigLoader:
    
    PROJECT_ROOT = Path(os.path.dirname(__file__)).parent
    default_config_path = os.path.join(PROJECT_ROOT, "config", "app_config.toml")

    @staticmethod
    def get_toml_file(): 
        try:
            with open(ConfigLoader.default_config_path, "rb") as f:
                return tomli.load(f)
        except Exception as error:
            print(f"Error => get_toml_file: {error}")
            return {}
        
    @staticmethod
    def get_config() -> AppConfig:
        try:
            config = AppConfig(**ConfigLoader.get_toml_file())
            return config
    
        except Exception as err:
            print(err)

        return None
