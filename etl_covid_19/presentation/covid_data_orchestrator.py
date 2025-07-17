from etl_covid_19.domain.use_cases.fetch_covid_data_usecase import FetchCovidDataUseCase
from etl_covid_19.domain.use_cases.transform_covid_data_usecase import TransformCovidDataUseCase
from etl_covid_19.domain.use_cases.insert_covid_data_use_case import InsertCovidDataUseCase

class CovidDataOrchestrator:
    def __init__(self,
                 fetch_use_case: FetchCovidDataUseCase,
                 transform_use_case: TransformCovidDataUseCase,
                 insert_use_case: InsertCovidDataUseCase):
        
        self.fetch_use_case = fetch_use_case
        self.transform_use_case = transform_use_case
        self.insert_use_case = insert_use_case

    def run(self):
        raw_data = self.fetch_use_case.execute()
        records = self.transform_use_case.execute(raw_data)
        self.insert_use_case.execute(records)
        return len(records)
