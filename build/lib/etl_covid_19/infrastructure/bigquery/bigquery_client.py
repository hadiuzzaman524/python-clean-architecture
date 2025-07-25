from typing import List, Dict, Optional
from google.cloud import bigquery
from google.oauth2 import service_account

class BigQueryClient:
    def __init__(self, service_account_path: str, project_id: str):
        """
        Initialize BigQuery client using service account credentials.
        """

        try:
            credentials = service_account.Credentials.from_service_account_file(service_account_path)
            self.client = bigquery.Client(credentials=credentials, project=project_id)
       
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
            return None
 
