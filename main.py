from etl_covid_19.domain.use_cases.fetch_covid_data_usecase import FetchCovidDataUseCase
from etl_covid_19.data.repository.covid_data_pipeline_impl import CovidDataPipelineImpl
from etl_covid_19.data.data_source.covid_data_source import CovidDataSource
from etl_covid_19.infrastructure.biqquery.bigquery_client import BigQueryClient
from etl_covid_19.infrastructure.database.database_client import DatabaseClient


bg = BigQueryClient()
db = DatabaseClient()
data_source = CovidDataSource(bigquery_client=bg)
pipeline = CovidDataPipelineImpl(data_source=data_source, database_client=db)
obj = FetchCovidDataUseCase(pipeline=pipeline)

data= obj.execute()
print(data)
