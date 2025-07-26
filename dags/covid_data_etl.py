import pendulum
from airflow.decorators import dag, task
from etl_covid_19.presentation.covid_data_orchestrator import CovidDataOrchestrator

@dag(
    schedule="0 6 * * *",  
    start_date=pendulum.datetime(2025, 7, 24, tz="UTC"),
    catchup=True,
    tags=["covid", "etl"],
)
def covid_data_pipeline():

    @task()
    def orchestrate(exec_date: str):
        # Convert exec_date (string) to pendulum datetime
        end_date = pendulum.parse(exec_date)
        start_date = end_date.subtract(days=2)

        orch = CovidDataOrchestrator(
            start_date=start_date,  
            end_date= end_date
        )
        return orch.trigger()

    orchestrate("{{ ds }}")

covid_data_pipeline()