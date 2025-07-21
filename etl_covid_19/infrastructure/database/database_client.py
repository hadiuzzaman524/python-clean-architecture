from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from config.app_config import config
from sqlalchemy.dialects.postgresql import insert

class DatabaseClient:
    def __init__(self):
        self.pg_config = config.postgres
        self.engine = create_engine(
            f"postgresql://{self.pg_config.USERNAME}:{quote_plus(self.pg_config.PASSWORD)}@"
            f"{self.pg_config.HOST}:{self.pg_config.PORT}/{self.pg_config.DB_NAME}"
        )
        # sessionmaker factory
        self.SessionLocal = sessionmaker(bind=self.engine)

    def bulk_upsert(self, model, records, conflict_columns):
        if not records:
            return
        
        table = model.__table__
        stmt = insert(table).values(records)
        update_dict = {
            c.name: stmt.excluded[c.name]
            for c in table.columns if c.name not in conflict_columns
        }
        stmt = stmt.on_conflict_do_update(
            index_elements=conflict_columns,
            set_=update_dict
        )

        session = self.SessionLocal()  # create session instance
        try:
            session.execute(stmt)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error => bulk_upsert: {e}")
            raise
        finally:
            session.close()

    def insert_data_into_pg(self, model_name, data):
        """Insert single record or list of records into database"""
        session = self.SessionLocal()
        try:
            if isinstance(data, list):
                instances = [model_name(**record) for record in data]
                session.bulk_save_objects(instances)
            else:
                instance = model_name(**data)
                session.add(instance)
            session.commit()
        except Exception as error:
            session.rollback()
            print(f"Error => insert_into_db: {error}")
            raise
        finally:
            session.close()

    def get_data_from_pg(self, model_name, query_filter: list = None, columns: list = None, limit: int = None):
        """
        Get data from database
        """
        session = self.SessionLocal()
        try:
            query = session.query(*columns) if columns else session.query(model_name)
            if query_filter:
                query = query.filter(*query_filter)
            if limit:
                query = query.limit(limit)
            return query.all()
        except Exception as error:
            print(f"Error => get_data_from_db: {error}")
            raise
        finally:
            session.close()

    def update_data_into_pg(self, model_name, query_filter: list, update_data: dict):
        """
        Update data
        Returns count of updated rows
        """
        session = self.SessionLocal()
        update_count = 0
        try:
            update_count = session.query(model_name).filter(*query_filter).update(update_data)
            session.commit()
            return update_count
        except Exception as error:
            session.rollback()
            print(f"Error => update_data: {error}")
            raise
        finally:
            session.close()

    def bulk_update_data_into_pg(self, model_name, query_filter: list, update_data: dict):
        """Bulk update"""
        session = self.SessionLocal()
        try:
            session.query(model_name).filter(*query_filter).update(update_data, synchronize_session=False)
            session.commit()
        except Exception as error:
            session.rollback()
            print(f"Error => bulk_update_data: {error}")
            raise
        finally:
            session.close()
