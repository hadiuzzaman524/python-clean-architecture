from etl_covid_19.service_locator import ServiceLocator
from etl_covid_19.presentation.base_cron_job import BaseCronJob

class CovidDataOrchestrator(BaseCronJob):

    def __init__(self, *args, **kwargs):
        self.start_date = kwargs.get('start_date')
        self.end_date = kwargs.get('end_date')

    def trigger(self):

        locator = ServiceLocator()

        extract = locator.fetch_covid_data_use_case()
        transform = locator.transform_covid_data_use_case()
        load = locator.insert_covid_data_use_case()

        try: 

            result = extract.execute(start_date=self.start_date, end_date= self.end_date)
            output= transform.execute(raw_data=result)
            load.execute(records=output)

        except Exception as e: 
            print(e)
            return False
        
        return True

