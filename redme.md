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
ORDER BY date DESC
LIMIT 100


**RUN CRON**
python main.py --cron-name covid_data_orchestrator --start-date 2020-08-01 --end-date 2020-08-02

**TEST COVERAGE**
PYTHONPATH=$(pwd) pytest --cov=etl_covid_19 --cov-report=term-missing test/
