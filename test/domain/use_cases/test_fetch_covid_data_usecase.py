import json
import pytest
from pathlib import Path
from etl_covid_19.domain.use_cases.fetch_covid_data_usecase import FetchCovidDataUseCase
from etl_covid_19.container import Container

class TestFetchCovidDataUseCase:

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        path = Path(__file__).parent.parent.parent / "mocks" / "covid_data_bigquery_sample.json"
        with path.open() as f:
            self.mock_data = json.load(f)

        self.mock_pipeline = mocker.Mock()
        self.mock_pipeline.fetch_from_bigquery.return_value = self.mock_data
        self.use_case = FetchCovidDataUseCase(pipeline=self.mock_pipeline)
        self.container = Container()

    def test_execute_returns_bigquery_result(self):
        result = self.use_case.execute(start_date="2020-07-01", end_date="2020-07-01")

        self.mock_pipeline.fetch_from_bigquery.assert_called_once_with(
            start_date="2020-07-01", end_date="2020-07-01"
        )
        assert result == self.mock_data
    
    def test_fetch_covid_data_use_case(self): 
        fetch_data_usecase = self.container.fetch_covid_data_use_case()
        result = fetch_data_usecase.execute(start_date='2020-07-01', end_date='2020-07-02')

        assert isinstance(result, list)
        assert len(result) > 0
        assert "country_code" in result[0]
        assert "date" in result[0]


