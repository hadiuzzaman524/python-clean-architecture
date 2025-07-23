import pytest
from unittest.mock import Mock
from etl_covid_19.data.repository.covid_data_pipeline_impl import CovidDataPipelineImpl
from etl_covid_19.domain.value_objects.covid_daily_record import CovidDailyRecord

class TestCovidDataPipelineImpl:

    @pytest.fixture(autouse=True)
    def setup(self, covid_bigquery_mock_data):
        self.mock_data_source = Mock()
        self.mock_db_client = Mock()
        self.pipeline = CovidDataPipelineImpl(self.mock_data_source, self.mock_db_client)
        self.raw_data = covid_bigquery_mock_data
        self.records = [
            CovidDailyRecord(**self.raw_data[0])
        ]

    def test_transform_records_removes_duplicates_and_returns_value_objects(self):
        result = self.pipeline.transform_records(self.raw_data)
        assert isinstance(result, list)
        assert len(result) == 1 
        assert isinstance(result[0], CovidDailyRecord)
        assert result[0].country_code == "RW"

    def test_load_to_database_calls_bulk_upsert_and_returns_count(self):

        result = self.pipeline.load_to_database(self.records)
        self.mock_db_client.bulk_upsert.assert_called_once()
        assert result == 1