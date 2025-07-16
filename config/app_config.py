from pydantic import BaseModel
from config.config_loader import ConfigLoader


class PostgresConfig(BaseModel):
    HOST: str
    USERNAME: str
    PASSWORD: str
    PORT: str
    DB_NAME: str

class AppConfig(BaseModel):
    postgress : PostgresConfig


config = ConfigLoader.get_config()