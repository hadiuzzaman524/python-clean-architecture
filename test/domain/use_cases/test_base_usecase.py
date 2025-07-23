from etl_covid_19.domain.use_cases.base_use_case import BaseUseCase
import pytest

class DummyUsecase(BaseUseCase): 
    def execute(self, *args, **kwargs):
        return super().execute(*args, **kwargs)
    
class TestBaseUsecase: 

    @pytest.fixture(autouse=True)
    def setup(self): 
        self.usecase = DummyUsecase()

    def test_base_use_case(self): 

        with pytest.raises(NotImplementedError): 
            self.usecase.execute()
