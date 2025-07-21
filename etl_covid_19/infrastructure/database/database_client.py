from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from config.app_config import config

class DatabaseClient:
    def __init__(self):
        self.pg_config = config.postgres
        self.engine = create_engine(
            f"postgresql://{self.pg_config.USERNAME}:{quote_plus(self.pg_config.PASSWORD)}@"
            f"{self.pg_config.HOST}:{self.pg_config.PORT}/{self.pg_config.DB_NAME}"
        )
        self.session = sessionmaker(bind=self.engine)

    def close_session(self): 
        if self.session.is_active:
            self.session.close()

    def insert_data_into_pg(self, model_name, data: dict):
        """Insert data into database"""
        try:
            queryset = model_name(**data)
            self.session.add(queryset)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            print(f"Error => insert_into_db: {error}")
    
    def get_data_from_pg(
        self,
        model_name,
        query_filter: list,
        columns: list,
        limit: int = None,
    ):
        """
        Get data from database
        """
        try:
            query = (
                self.session.query(*columns)
                if columns
                else self.session.query(model_name)
            )
            query = query.filter(*query_filter)

            if limit:
                query = query.limit(limit)
            return query.all()
        
        except Exception as error:
            print(f"Error => get_data_from_db: {error}")

    def update_data_into_pg(self, model_name, query_filter: list, update_data: dict):
        """
        Update data

        query_filter: list => pass an empty list if you don't want to filter
        :rtype count of updated row(s)
        """

        update_count = 0
        try:
            update_count = (
                self.session.query(model_name)
                .filter(*query_filter)
                .update(update_data)
            )
            self.session.commit()

        except Exception as error:
            print(f"Error => update_data: {error}")
            self.session.rollback()

        return update_count

    def bulk_update_data_into_pg(
        self, model_name, query_filter: list, update_data: dict
    ):
        """Bulk update"""
        try:
            self.session.query(model_name).filter(*query_filter).update(
                update_data,
                synchronize_session=False,
            )
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            print(f"bulk_update_data: {error}")
