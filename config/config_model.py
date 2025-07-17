from pydantic import BaseModel

class PostgresConfig(BaseModel):
    HOST: str
    USERNAME: str
    PASSWORD: str
    PORT: str
    DB_NAME: str


class BigQueryConfig(BaseModel):
    PROJECT_ID:str
    SERVICE_ACCOUNT_FILEPATH: str

class AppConfig(BaseModel):
    postgres : PostgresConfig
    bigquery: BigQueryConfig


