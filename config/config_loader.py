from typing import Optional
from config.app_config import AppConfig
import tomli
from pathlib import Path
import os


class ConfigLoader:
    
    PROJECT_ROOT = Path(os.path.dirname(__file__)).parent.parent
    default_config_path = os.path.join(PROJECT_ROOT, "config", "app_config.toml")

    def get_toml_file(self): 
        try:
            with open(self.default_config_path, "rb") as f:
                return tomli.load(f)
        except Exception as error:
            print(f"Error => get_toml_file: {error}")
            return {}
        
    @staticmethod
    def get_config() -> Optional[AppConfig]:
        try:
            config = AppConfig(**ConfigLoader.get_toml_file())
            return config
    
        except Exception as err:
            print(err)

        return None
