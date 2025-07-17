from typing import List
from etl_covid_19.domain.use_cases.base_use_case import BaseUseCase
from etl_covid_19.domain.services.covid_data_pipeline import CovidDataPipeline
from etl_covid_19.domain.value_objects.covid_daily_record import CovidDailyRecord

class InsertCovidDataUseCase(BaseUseCase):
    def __init__(self, pipeline: CovidDataPipeline):
        self.pipeline = pipeline

    def execute(self, records: List[CovidDailyRecord]) -> None:
        self.pipeline.load_to_database(records)
