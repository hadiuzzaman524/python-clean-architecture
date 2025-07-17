from etl_covid_19.infrastructure.database.database_client import DatabaseClient

db = DatabaseClient()

print(db.session)