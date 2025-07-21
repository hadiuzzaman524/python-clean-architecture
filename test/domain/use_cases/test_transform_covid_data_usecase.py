from unittest.mock import Mock
from etl_covid_19.domain.use_cases.transform_covid_data_usecase import TransformCovidDataUseCase
from etl_covid_19.domain.value_objects.covid_daily_record import CovidDailyRecord

def test_execute_transforms_raw_data_to_value_objects():
    pipeline = Mock()
    expected = [CovidDailyRecord(
        date="2024-01-01",
        country_code="US",
        country_name="United States",
        new_confirmed=100,
        new_deceased=5,
        cumulative_deceased=50,
        cumulative_tested=1000,
        population_male=500000,
        population_female=520000,
        smoking_prevalence=0.2,
        diabetes_prevalence=0.05
    )]
    pipeline.transform_records.return_value = expected
    usecase = TransformCovidDataUseCase(pipeline)
    raw_data = [{
        "date": "2024-01-01",
        "country_code": "US",
        "country_name": "United States",
        "new_confirmed": 100,
        "new_deceased": 5,
        "cumulative_deceased": 50,
        "cumulative_tested": 1000,
        "population_male": 500000,
        "population_female": 520000,
        "smoking_prevalence": 0.2,
        "diabetes_prevalence": 0.05
    }]
    result = usecase.execute(raw_data)
    assert result == expected
    pipeline.transform_records.assert_called_once()