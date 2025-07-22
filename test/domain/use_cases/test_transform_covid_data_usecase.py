import pytest
from unittest.mock import Mock
from etl_covid_19.domain.use_cases.transform_covid_data_usecase import TransformCovidDataUseCase
from etl_covid_19.domain.value_objects.covid_daily_record import CovidDailyRecord
from etl_covid_19.container import Container

class TestTransformCovidDataUseCase:

    @pytest.fixture(autouse=True)
    def setup(self, covid_bigquery_mock_data):

        self.raw_data = covid_bigquery_mock_data

        self.expected_result = [CovidDailyRecord(
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
        self.mock_pipeline.transform_records.return_value = self.expected_result
        self.usecase = TransformCovidDataUseCase(self.mock_pipeline)
        self.container = Container()

    def test_execute_transforms_raw_data_to_value_objects(self):
        """Unit test: check use case with mocked pipeline."""

        result = self.usecase.execute(self.raw_data)
        assert result == self.expected_result
        self.mock_pipeline.transform_records.assert_called_once_with(self.raw_data)
    
    def test_transform_covid_data_usecase(self): 
        """Integration test: check real use case from container."""
        
        transform_usecase = self.container.transform_covid_data_use_case()
        result = transform_usecase.execute(raw_data=self.raw_data)
        assert result
        assert len(result) >= 1

