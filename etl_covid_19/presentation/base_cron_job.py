from abc import ABC, abstractmethod

class BaseCronJob(ABC):
    def __init__(self,*args, **kwargs):
        pass
    
    @abstractmethod
    def trigger(self):
        raise NotImplementedError("Subclasses must implement trigger()")
