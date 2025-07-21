from etl_covid_19.domain.services.covid_data_pipeline import CovidDataPipeline
from etl_covid_19.data.data_source.covid_data_source import CovidDataSource
from etl_covid_19.infrastructure.database.database_client import DatabaseClient
from etl_covid_19.data.model.covid_model import CovidModel
import pandas as pd 

class CovidDataPipelineImpl(CovidDataPipeline):
    
    def __init__(self, data_source: CovidDataSource, database_client: DatabaseClient):
        self.data_source = data_source
        self.database_client = database_client
  
    def fetch_from_bigquery(self):
        return self.data_source.get_data_from_big_query()
        
    def transform_records(self, raw_data):
        df = pd.DataFrame(raw_data)
        df = df.fillna(0).infer_objects(copy=False)
        return df.to_dict(orient="records")

    def load_to_database(self, records):
        self.database_client.insert_data_into_pg(model_name= CovidModel, data= records)
    