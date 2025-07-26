import pytest
from unittest.mock import MagicMock, patch

from etl_covid_19.presentation.base_cron_job import BaseCronJob
from etl_covid_19.presentation.covid_data_orchestrator import CovidDataOrchestrator


class TestCovidDataOrchestrator:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.start_date = "2024-01-01"
        self.end_date = "2024-01-31"
        self.orchestrator = CovidDataOrchestrator(
            start_date=self.start_date,
            end_date=self.end_date
        )

    @patch("etl_covid_19.presentation.covid_data_orchestrator.ServiceLocator")
    def test_trigger_success(self, mock_container_cls):

        mock_container = MagicMock()
        mock_extract = MagicMock()
        mock_transform = MagicMock()
        mock_load = MagicMock()

        mock_extract.execute.return_value = "raw_data"
        mock_transform.execute.return_value = "processed_data"
        mock_container.fetch_covid_data_use_case.return_value = mock_extract
        mock_container.transform_covid_data_use_case.return_value = mock_transform
        mock_container.insert_covid_data_use_case.return_value = mock_load
        mock_container_cls.return_value = mock_container
        self.orchestrator.trigger()
        mock_extract.execute.assert_called_once_with(start_date=self.start_date, end_date=self.end_date)
        mock_transform.execute.assert_called_once_with(raw_data="raw_data")
        mock_load.execute.assert_called_once_with(records="processed_data")

    @patch("etl_covid_19.presentation.covid_data_orchestrator.ServiceLocator")
    def test_trigger_with_exception(self, mock_container_cls, capsys):
   
        mock_container = MagicMock()
        mock_extract = MagicMock()
        mock_extract.execute.side_effect = RuntimeError("Extraction failed")
        mock_container.fetch_covid_data_use_case.return_value = mock_extract
        mock_container.transform_covid_data_use_case.return_value = MagicMock()
        mock_container.insert_covid_data_use_case.return_value = MagicMock()
        mock_container_cls.return_value = mock_container
        result = self.orchestrator.trigger()
        assert result is False
