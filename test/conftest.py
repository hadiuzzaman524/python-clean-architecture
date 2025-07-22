import pytest
import json
from pathlib import Path

@pytest.fixture
def covid_bigquery_mock_data():
    path = Path(__file__).parent / "mocks" / "covid_data_bigquery_sample.json"
    with path.open() as f:
        return json.load(f)
