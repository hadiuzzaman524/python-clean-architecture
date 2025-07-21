from sqlalchemy import Column, String, Date, Integer, Float
from etl_covid_19.data.model.base_db_model import BaseDbModel

class CovidModel(BaseDbModel):
    __tablename__ = "covid_daily_records"

    # Composite Primary Key
    date = Column(Date, primary_key=True, nullable=False)
    country_code = Column(String(10), primary_key=True, nullable=False)

    country_name = Column(String(100), nullable=True)
    new_confirmed = Column(Integer, nullable=True)
    new_deceased = Column(Integer, nullable=True)
    cumulative_deceased = Column(Integer, nullable=True)
    cumulative_tested = Column(Integer, nullable=True)
    population_male = Column(Integer, nullable=True)
    population_female = Column(Integer, nullable=True)
    smoking_prevalence = Column(Float, nullable=True)
    diabetes_prevalence = Column(Float, nullable=True)

