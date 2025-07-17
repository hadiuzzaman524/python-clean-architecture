from etl_covid_19.domain.services.covid_data_pipeline import CovidDataPipeline
from etl_covid_19.data.data_source.covid_data_source import CovidDataSource

class CovidDataPipelineImpl(CovidDataPipeline):
    def __init__(self, data_source: CovidDataSource):
        self.data_source = data_source
  

    def fetch_from_bigquery(self):
        return self.data_source.get_data_from_big_query()
    
    def transform_records(self, raw_data):
        return super().transform_records(raw_data)
    
    def load_to_database(self, records):
        return super().load_to_database(records)