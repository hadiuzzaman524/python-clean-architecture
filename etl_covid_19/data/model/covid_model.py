from sqlalchemy import Column, String, Date, Integer, Float, UniqueConstraint
from etl_covid_19.data.model.base_db_model import BaseDbModel

class CovidModel(BaseDbModel):

    date = Column(Date, nullable=False)
    country_code = Column(String(10), nullable=False)
    country_name = Column(String(100), nullable=False)
    new_confirmed = Column(Integer, nullable=False)
    new_deceased = Column(Integer, nullable=False)
    cumulative_deceased = Column(Integer, nullable=False)
    cumulative_tested = Column(Integer, nullable=False)
    population_male = Column(Integer, nullable=False)
    population_female = Column(Integer, nullable=False)
    smoking_prevalence = Column(Float, nullable=True)
    diabetes_prevalence = Column(Float, nullable=True)
    
    __tablename__ = "covid_daily_records"
    __table_args__ = (
        UniqueConstraint("date", "country_code", name="uix_date_country_code"),
    )
