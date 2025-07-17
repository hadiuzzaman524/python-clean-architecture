from pydantic import BaseModel
from datetime import date
from typing import Optional

class CovidDailyRecord(BaseModel):
    date: date
    country_code: str
    country_name: str
    new_confirmed: int
    new_deceased: int
    cumulative_deceased: int
    cumulative_tested: int
    population_male: int
    population_female: int
    smoking_prevalence: Optional[float] = None
    diabetes_prevalence: Optional[float] = None
