from pydantic import BaseModel

class PostgresConfig(BaseModel):
    HOST: str
    USERNAME: str
    PASSWORD: str
    PORT: str
    DB_NAME: str

class AppConfig(BaseModel):
    postgress_config : PostgresConfig
