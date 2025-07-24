from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from sqlalchemy.dialects.postgresql import insert

class DatabaseClient:
    def __init__(self, 
                 user_name:str, 
                 password:str, 
                 host:str, 
                 port:str, 
                 db_name: str
        ):

        self.engine = create_engine(
            f"postgresql://{user_name}:{quote_plus(password)}@"
            f"{host}:{port}/{db_name}"
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
