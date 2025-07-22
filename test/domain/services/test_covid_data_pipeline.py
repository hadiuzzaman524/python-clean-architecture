import pytest
from etl_covid_19.domain.services.covid_data_pipeline import CovidDataPipeline

class DummyPipeline(CovidDataPipeline):
    def fetch_from_bigquery(self, start_date: str, end_date: str):
        super().fetch_from_bigquery(start_date, end_date)
    def transform_records(self, raw_data):
        super().transform_records(raw_data)
    def load_to_database(self, records):
        super().load_to_database(records)

def test_abstract_methods_raise_not_implemented():
    dummy = DummyPipeline()
    with pytest.raises(NotImplementedError):
        dummy.fetch_from_bigquery("2020-01-01", "2020-01-02")
    with pytest.raises(NotImplementedError):
        dummy.transform_records([{}])
    with pytest.raises(NotImplementedError):
        dummy.load_to_database([])