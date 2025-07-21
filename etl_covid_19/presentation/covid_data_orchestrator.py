from etl_covid_19.container import Container

class CovidDataOrchestrator:

    container = Container()
    
    try: 
        extract = container.fetch_covid_data_use_case()
        transform = container.transform_covid_data_use_case()
        load = container.insert_covid_data_use_case()

        result = extract.execute(start_date='2020-05-01', end_date='2020-05-05')
        output= transform.execute(raw_data=result)
        load.execute(records=output)

    except Exception as e: 
        print(e)

