from unittest.mock import patch, Mock, MagicMock
from etl_covid_19.infrastructure.bigquery.bigquery_client import BigQueryClient

class TestBigQueryClient:

    @patch("etl_covid_19.infrastructure.bigquery.bigquery_client.service_account.Credentials")
    @patch("etl_covid_19.infrastructure.bigquery.bigquery_client.bigquery.Client")
    def test_init_success(self, mock_bq_client, mock_credentials):
        mock_credentials.from_service_account_file.return_value = Mock()
        client = BigQueryClient("fake/path.json", "test-project")
        mock_bq_client.assert_called_once()

    @patch("etl_covid_19.infrastructure.bigquery.bigquery_client.bigquery.Client")
    def test_init_failure(self, mock_bq_client):
        with patch("etl_covid_19.infrastructure.bigquery.bigquery_client.service_account.Credentials.from_service_account_file", side_effect=Exception("fail")):
            client = BigQueryClient("bad/path.json", "test-project")


    @patch("etl_covid_19.infrastructure.bigquery.bigquery_client.service_account.Credentials")
    @patch("etl_covid_19.infrastructure.bigquery.bigquery_client.bigquery.Client")
    def test_run_query_success(self, mock_bq_client, mock_credentials):
       
        mock_credentials.from_service_account_file.return_value = Mock()
        mock_client_instance = mock_bq_client.return_value

        mock_row = MagicMock()
        mock_row.keys.return_value = ["field"]
        mock_row.__getitem__.side_effect = lambda key: {"field": "value"}[key]

        mock_query_job = Mock()
        mock_query_job.result.return_value = [mock_row]
        mock_client_instance.query.return_value = mock_query_job

        client = BigQueryClient("fake/path.json", "test-project")
        result = client.run_query("SELECT 1")

        assert result == [{"field": "value"}]


    @patch("etl_covid_19.infrastructure.bigquery.bigquery_client.bigquery.Client")
    def test_run_query_failure(self, mock_bq_client):
        mock_client_instance = mock_bq_client.return_value
        mock_client_instance.query.side_effect = Exception("Query failed")

        client = BigQueryClient("fake/path.json", "test-project")
        result = client.run_query("SELECT 1")
        assert result is None or result == []