from typing import List
from etl_covid_19.domain.use_cases.base_use_case import BaseUseCase
from etl_covid_19.domain.services.covid_data_pipeline import CovidDataPipeline

class FetchCovidDataUseCase(BaseUseCase):
    def __init__(self, pipeline: CovidDataPipeline):
        self.pipeline = pipeline

    def execute(self) -> List[dict]:
        return self.pipeline.fetch_from_bigquery()