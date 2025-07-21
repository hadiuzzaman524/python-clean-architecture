import pandas as pd 
from etl_covid_19.domain.services.covid_data_pipeline import CovidDataPipeline
from etl_covid_19.data.data_source.covid_data_source import CovidDataSource
from etl_covid_19.infrastructure.database.database_client import DatabaseClient
from etl_covid_19.data.model.covid_model import CovidModel
from etl_covid_19.domain.value_objects.covid_daily_record import CovidDailyRecord

class CovidDataPipelineImpl(CovidDataPipeline):
    
    def __init__(self, data_source: CovidDataSource, database_client: DatabaseClient):
        self.data_source = data_source
        self.database_client = database_client
  
    
    def fetch_from_bigquery(self,start_date: str, end_date: str):
        return self.data_source.get_data_from_big_query(start_date=start_date, end_date=end_date)
        
    def transform_records(self, raw_data):
        df = pd.DataFrame(raw_data)
        df = df.fillna(0).infer_objects(copy=False)
        df = df.drop_duplicates(subset=["date", "country_code"], keep="first")
        return [CovidDailyRecord(**item) for item in df.to_dict(orient="records")]

    def load_to_database(self, records):
        records_as_dicts = [record.__dict__ for record in records]
        self.database_client.bulk_upsert(
            model=CovidModel,
            records=records_as_dicts,
            conflict_columns=['date', 'country_code']
        )