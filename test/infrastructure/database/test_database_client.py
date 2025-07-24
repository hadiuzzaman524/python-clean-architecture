import pytest
from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session
from etl_covid_19.infrastructure.database.database_client import DatabaseClient

class DummyModel:
    __tablename__ = 'dummy'
    __table__ = MagicMock()
    id = 1
    name = 'Test'

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)



