import pytest
from unittest.mock import patch, Mock, MagicMock
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from etl_covid_19.infrastructure.database.database_client import DatabaseClient

Base = declarative_base()

class DummyModel(Base):
    __tablename__ = "dummy_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class TestDatabaseClient:

    def test_init_creates_engine_with_url_encoding(self):
        with patch("etl_covid_19.infrastructure.database.database_client.create_engine") as mock_create_engine, \
             patch("etl_covid_19.infrastructure.database.database_client.sessionmaker") as mock_sessionmaker:
            
            DatabaseClient(
                user_name="user",
                password="pass@123",
                host="localhost",
                port="5432",
                db_name="testdb"
            )

            expected_url = "postgresql://user:pass%40123@localhost:5432/testdb"
            mock_create_engine.assert_called_once_with(expected_url)
            mock_sessionmaker.assert_called_once_with(bind=mock_create_engine.return_value)

    def test_bulk_upsert_returns_early_on_empty_records(self):
        with patch("etl_covid_19.infrastructure.database.database_client.create_engine"), \
             patch("etl_covid_19.infrastructure.database.database_client.sessionmaker"):

            client = DatabaseClient("user", "pass", "localhost", "5432", "testdb")
            result = client.bulk_upsert(DummyModel, [], ["id"])
            assert result is None

    def test_bulk_upsert_success(self):
        mock_session = Mock()
        mock_session.execute = Mock()
        mock_session.commit = Mock()
        mock_session.rollback = Mock()
        mock_session.close = Mock()

        mock_sessionmaker = Mock(return_value=mock_session)

        with patch("etl_covid_19.infrastructure.database.database_client.create_engine"), \
             patch("etl_covid_19.infrastructure.database.database_client.sessionmaker", return_value=mock_sessionmaker), \
             patch("etl_covid_19.infrastructure.database.database_client.insert") as mock_insert:

            # Setup mock insert stmt and on_conflict_do_update chain
            mock_stmt = MagicMock()
            mock_insert.return_value = mock_stmt
            mock_stmt.values.return_value = mock_stmt
            mock_stmt.on_conflict_do_update.return_value = mock_stmt
            # Mock excluded attribute for update_dict construction
            mock_stmt.excluded = {"name": "excluded_name", "email": "excluded_email"}

            client = DatabaseClient("user", "pass", "localhost", "5432", "testdb")

            records = [
                {"id": 1, "name": "Alice", "email": "alice@example.com"},
                {"id": 2, "name": "Bob", "email": "bob@example.com"},
            ]

            client.bulk_upsert(DummyModel, records, ["id"])

            mock_insert.assert_called_once_with(DummyModel.__table__)
            mock_stmt.values.assert_called_once_with(records)
            mock_stmt.on_conflict_do_update.assert_called_once()
            mock_session.execute.assert_called_once_with(mock_stmt)
            mock_session.commit.assert_called_once()
            mock_session.close.assert_called_once()
            mock_session.rollback.assert_not_called()

    def test_bulk_upsert_exception_handling(self):
        mock_session = Mock()
        mock_session.execute = Mock(side_effect=Exception("DB error"))
        mock_session.commit = Mock()
        mock_session.rollback = Mock()
        mock_session.close = Mock()

        mock_sessionmaker = Mock(return_value=mock_session)

        with patch("etl_covid_19.infrastructure.database.database_client.create_engine"), \
             patch("etl_covid_19.infrastructure.database.database_client.sessionmaker", return_value=mock_sessionmaker), \
             patch("builtins.print") as mock_print, \
             patch("etl_covid_19.infrastructure.database.database_client.insert") as mock_insert:

            mock_stmt = MagicMock()
            mock_insert.return_value = mock_stmt
            mock_stmt.values.return_value = mock_stmt
            mock_stmt.on_conflict_do_update.return_value = mock_stmt
            mock_stmt.excluded = {"name": "excluded_name", "email": "excluded_email"}

            client = DatabaseClient("user", "pass", "localhost", "5432", "testdb")

            records = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]

            with pytest.raises(Exception, match="DB error"):
                client.bulk_upsert(DummyModel, records, ["id"])

            mock_session.rollback.assert_called_once()
            mock_session.close.assert_called_once()
            mock_session.commit.assert_not_called()
            mock_print.assert_called_once()
