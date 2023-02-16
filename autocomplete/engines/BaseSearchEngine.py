from ..utils import Dictionary

from abc import ABC
from abc import abstractmethod

class BaseSearchEngine(ABC):
    def __init__(self, dictionary: Dictionary) -> None:
        self.dictionary = dictionary
        
        self.max_suggestions = 3

    @abstractmethod
    def search(self, prefix: str) -> list[str]:
        raise NotImplementedError("Subclass should implement this!")
