from dependency_injector import containers, providers

from etl_covid_19.domain.use_cases.fetch_covid_data_usecase import FetchCovidDataUseCase
from etl_covid_19.domain.use_cases.transform_covid_data_usecase import TransformCovidDataUseCase
from etl_covid_19.domain.use_cases.insert_covid_data_use_case import InsertCovidDataUseCase

from etl_covid_19.data.repository.covid_data_pipeline_impl import CovidDataPipelineImpl
from etl_covid_19.data.data_source.covid_data_source import CovidDataSource

from etl_covid_19.infrastructure.bigquery.bigquery_client import BigQueryClient
from etl_covid_19.infrastructure.database.database_client import DatabaseClient
from config.app_config import config


class Container(containers.DeclarativeContainer):

    bigquery_config = config.bigquery
    
    # Infrastructure clients
    bigquery_client = providers.Singleton(
        BigQueryClient, 
        service_account_path = bigquery_config.SERVICE_ACCOUNT_FILEPATH,
        project_id = bigquery_config.PROJECT_ID
    )
    database_client = providers.Singleton(DatabaseClient)
    
    # Data source with dependency on bigquery client
    covid_data_source = providers.Factory(
        CovidDataSource,
        bigquery_client=bigquery_client,
    )
    
    # Repository / pipeline implementation with dependencies
    covid_data_pipeline = providers.Factory(
        CovidDataPipelineImpl,
        data_source=covid_data_source,
        database_client=database_client,
    )
    
    # Use cases with pipeline dependency
    fetch_covid_data_use_case = providers.Factory(
        FetchCovidDataUseCase,
        pipeline=covid_data_pipeline,
    )
    
    transform_covid_data_use_case = providers.Factory(
        TransformCovidDataUseCase,
        pipeline=covid_data_pipeline,
    )
    
    insert_covid_data_use_case = providers.Factory(
        InsertCovidDataUseCase,
        pipeline=covid_data_pipeline,
    )
