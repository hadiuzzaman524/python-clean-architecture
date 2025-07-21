from etl_covid_19.infrastructure.biqquery.bigquery_client import BigQueryClient

class CovidDataSource:

    def __init__(self, bigquery_client: BigQueryClient):
        self.bigquery_client = bigquery_client
        
    def get_data_from_big_query(self, start_date: str, end_date: str):
        query = """ 
            SELECT
            date,
            country_code,
            country_name,
            new_confirmed,
            new_deceased,
            cumulative_deceased,
            cumulative_tested,
            population_male,
            population_female,
            smoking_prevalence,
            diabetes_prevalence
            FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
            WHERE date BETWEEN '{start_date}' AND '{end_date}'
            ORDER BY date DESC
        """.format(start_date=start_date, end_date=end_date)
        
        return self.bigquery_client.run_query(query=query)