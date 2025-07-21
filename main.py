import pandas as pd 

from etl_covid_19.domain.use_cases.fetch_covid_data_usecase import FetchCovidDataUseCase
from etl_covid_19.data.repository.covid_data_pipeline_impl import CovidDataPipelineImpl
from etl_covid_19.data.data_source.covid_data_source import CovidDataSource
from etl_covid_19.infrastructure.biqquery.bigquery_client import BigQueryClient
from etl_covid_19.infrastructure.database.database_client import DatabaseClient
from etl_covid_19.domain.use_cases.transform_covid_data_usecase import TransformCovidDataUseCase
from etl_covid_19.domain.use_cases.insert_covid_data_use_case import InsertCovidDataUseCase


bg = BigQueryClient()
db = DatabaseClient()
data_source = CovidDataSource(bigquery_client=bg)
pipeline = CovidDataPipelineImpl(data_source=data_source, database_client=db)

obj = FetchCovidDataUseCase(pipeline=pipeline)
transform = TransformCovidDataUseCase(pipeline=pipeline)
insert = InsertCovidDataUseCase(pipeline=pipeline)

data= obj.execute(start_date='2020-06-01', end_date='2020-06-05')
trans_data= transform.execute(data)
insert.execute(records=trans_data)

