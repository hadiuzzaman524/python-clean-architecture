import pytest
from etl_covid_19.domain.services.covid_data_pipeline import CovidDataPipeline

class DummyPipeline(CovidDataPipeline):
    def fetch_from_bigquery(self, start_date: str, end_date: str):
        super().fetch_from_bigquery(start_date, end_date)
    def transform_records(self, raw_data):
        super().transform_records(raw_data)
    def load_to_database(self, records):
        super().load_to_database(records)

class TestCovidDataPipeline:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dummy = DummyPipeline()

    def test_fetch_from_bigquery_raises(self):
        with pytest.raises(NotImplementedError):
            self.dummy.fetch_from_bigquery("2020-01-01", "2020-01-02")

    def test_transform_records_raises(self):
        with pytest.raises(NotImplementedError):
            self.dummy.transform_records([{}])

    def test_load_to_database_raises(self):
        with pytest.raises(NotImplementedError):
            self.dummy.load_to_database([])
