from typing import List, Dict, Optional
from google.cloud import bigquery
from google.oauth2 import service_account
from config.app_config import config

class BigQueryClient:
    def __init__(self):
        """
        Initialize BigQuery client using service account credentials.
        """
        self.config = config.bigquery
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.config.SERVICE_ACCOUNT_FILEPATH
            )
            self.client = bigquery.Client(credentials=credentials, project=self.config.PROJECT_ID)
       
        except Exception as error:
            print(f"Error initializing BigQuery client: {error}")
 

    def run_query(self, query: str) -> List[Dict]:
        """
        Run a SQL query and return results as a list of dictionaries.
        """
        try:
            query_job = self.client.query(query)
            results = query_job.result()
            return [dict(row) for row in results]
        except Exception as error:
            print(f"Error running query: {error}")
 
