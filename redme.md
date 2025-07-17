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