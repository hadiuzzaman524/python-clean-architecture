import pytest
from etl_covid_19.domain.use_cases.fetch_covid_data_usecase import FetchCovidDataUseCase
from etl_covid_19.container import Container
from unittest.mock import Mock

class TestFetchCovidDataUseCase:

    @pytest.fixture(autouse=True)
    def setup(self, covid_bigquery_mock_data):
        self.mock_data = covid_bigquery_mock_data
        self.mock_pipeline = Mock()
        self.mock_pipeline.fetch_from_bigquery.return_value = self.mock_data
        self.use_case = FetchCovidDataUseCase(pipeline=self.mock_pipeline)
        self.container = Container()

    def test_execute_returns_bigquery_result(self):
        """Unit test: verifies use case logic with mocked pipeline"""

        result = self.use_case.execute(start_date="2020-07-01", end_date="2020-07-01")

        self.mock_pipeline.fetch_from_bigquery.assert_called_once_with(
            start_date="2020-07-01", end_date="2020-07-01"
        )
        assert result == self.mock_data
    
    def test_fetch_covid_data_use_case(self): 
        """Integration test: verifies container and use case with real pipeline"""

        fetch_data_usecase = self.container.fetch_covid_data_use_case()
        result = fetch_data_usecase.execute(start_date='2020-07-01', end_date='2020-07-02')

        assert isinstance(result, list)
        assert len(result) > 0
        assert "country_code" in result[0]
        assert "date" in result[0]


