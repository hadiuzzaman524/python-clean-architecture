import pytest
from datetime import date
from pydantic import ValidationError
from etl_covid_19.domain.value_objects.covid_daily_record import CovidDailyRecord


class TestCovidDailyRecord:
    
    def test_valid(self):
        record = CovidDailyRecord(
            date=date(2024, 1, 1),
            country_code="US",
            country_name="United States",
            new_confirmed=100,
            new_deceased=5,
            cumulative_deceased=500,
            cumulative_tested=10000,
            population_male=150000,
            population_female=155000,
        )
        assert record.country_code == "US"
        assert record.new_confirmed == 100

    def test_invalid(self):
        try:
            CovidDailyRecord(
                date='2024-01-01',  # Invalid type, should be datetime.date
                country_code="US",
                country_name="United States",
                new_confirmed=100,
                new_deceased=5,
                cumulative_deceased=500,
                cumulative_tested=10000,
                population_male=150000,
                population_female=155000,
            )
        except ValidationError as e:
            assert "value is not a valid date" in str(e)

