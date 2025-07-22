import pytest
from unittest.mock import Mock
from etl_covid_19.domain.use_cases.insert_covid_data_use_case import InsertCovidDataUseCase
from etl_covid_19.domain.value_objects.covid_daily_record import CovidDailyRecord
from etl_covid_19.container import Container

class TestInsertCovidDataUsecase:

    @pytest.fixture(autouse=True)
    def setup(self, covid_bigquery_mock_data):
        self.raw_data = covid_bigquery_mock_data
        self.records = [CovidDailyRecord(
            date=record["date"],
            country_code=record["country_code"],
            country_name=record["country_name"],
            new_confirmed=record["new_confirmed"],
            new_deceased=record["new_deceased"],
            cumulative_deceased=record["cumulative_deceased"],
            cumulative_tested=record["cumulative_tested"],
            population_male=record["population_male"],
            population_female=record["population_female"],
            smoking_prevalence=record["smoking_prevalence"],
            diabetes_prevalence=record["diabetes_prevalence"]
        ) for record in self.raw_data]

        self.mock_pipeline = Mock()
        self.usecase = InsertCovidDataUseCase(pipeline= self.mock_pipeline)
        self.container = Container()
    
    def test_execute_calls_pipeline_with_records(self): 
        """Unit test: check use case with mocked pipeline."""

        self.usecase.execute(records= self.records)
        self.mock_pipeline.load_to_database.assert_called_once_with(self.records)

    def test_insert_covid_data_usecase(self):
        """Integration test: check real use case from container."""
        
        insert_usecase = self.container.insert_covid_data_use_case()
        len = insert_usecase.execute(records=self.records)
        assert len == 1
        


