from abc import ABC, abstractmethod
from typing import List
from etl_covid_19.domain.value_objects.covid_daily_record import CovidDailyRecord


class CovidDataPipeline(ABC):
    """
    Abstract base class for handling COVID data extraction,
    transformation, and loading (ETL).
    """

    @abstractmethod
    def fetch_from_bigquery(self) -> List[CovidDailyRecord]:
        """Extract COVID data from BigQuery"""
        pass

    @abstractmethod
    def transform_records(self, raw_data: List[dict]) -> List[CovidDailyRecord]:
        """Transform raw dicts into validated CovidDailyRecord objects"""
        pass

    @abstractmethod
    def load_to_database(self, records: List[CovidDailyRecord]) -> None:
        """Load processed data into the database"""
        pass
