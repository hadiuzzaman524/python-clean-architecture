from sqlalchemy import Column, String, Date, Integer, Float, UniqueConstraint
from etl_covid_19.data.model.base_db_model import BaseDbModel

class CovidModel(BaseDbModel):

    date = Column(Date, nullable=False)
    country_code = Column(String(10), nullable=True)
    country_name = Column(String(100), nullable=True)
    new_confirmed = Column(Integer, nullable=True)
    new_deceased = Column(Integer, nullable=True)
    cumulative_deceased = Column(Integer, nullable=True)
    cumulative_tested = Column(Integer, nullable=True)
    population_male = Column(Integer, nullable=True)
    population_female = Column(Integer, nullable=True)
    smoking_prevalence = Column(Float, nullable=True)
    diabetes_prevalence = Column(Float, nullable=True)
    
    __tablename__ = "covid_daily_records"
    __table_args__ = (
        UniqueConstraint("date", "country_code", name="uix_date_country_code"),
    )
