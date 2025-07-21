from unittest.mock import Mock
from etl_covid_19.domain.use_cases.fetch_covid_data_usecase import FetchCovidDataUseCase

def test_execute_returns_raw_data_list():
    pipeline = Mock()
    pipeline.fetch_from_bigquery.return_value = [{"foo": "bar"}]
    usecase = FetchCovidDataUseCase(pipeline)
    result = usecase.execute("2024-01-01", "2024-01-02")
    assert isinstance(result, list)
    assert result == [{"foo": "bar"}]
    pipeline.fetch_from_bigquery.assert_called_once_with(start_date="2024-01-01", end_date="2024-01-02")