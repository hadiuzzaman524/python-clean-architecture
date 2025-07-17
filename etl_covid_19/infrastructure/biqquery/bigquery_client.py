
from google.cloud import bigquery
from typing import List, Dict, Optional


class BigQueryClient:
    def __init__(self, project_id: Optional[str] = None):
        self.client = bigquery.Client(project=project_id)

    def run_query(self, query: str) -> List[Dict]:
        """Run a SQL query and return results as a list of dicts."""
        query_job = self.client.query(query)
        return [dict(row) for row in query_job.result()]
