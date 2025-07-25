import pytest
from etl_covid_19.presentation.base_cron_job import BaseCronJob

class DummyCronJob(BaseCronJob):
    def trigger(self):
        return super().trigger()


class TestBaseCronJob:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.cronjob = DummyCronJob()

    def test_trigger_not_implemented(self):
        with pytest.raises(NotImplementedError):
            self.cronjob.trigger()