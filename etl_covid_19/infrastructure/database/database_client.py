from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from config.app_config import config

class DatabaseClient:
    def __init__(self):
        self.pg_config = config.postgress
        self.engine = create_engine(
            f"postgresql://{self.pg_config.USERNAME}:{quote_plus(self.pg_config.PASSWORD)}@"
            f"{self.pg_config.HOST}:{self.pg_config.PORT}/{self.pg_config.DB_NAME}"
        )
        self.session = sessionmaker(bind=self.engine)

    def get_session(self): 
        return self.session
    
    def close_session(self): 
        if self.session.is_active:
            self.session.close()