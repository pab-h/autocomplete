from Dictionary import Dictionary
from abc import ABC
from abc import abstractmethod

class BaseSearchEngine(ABC):
    def __init__(self, dictionary: Dictionary) -> None:
        self._dictionary = dictionary
        self.__max_suggestions: int = 3

    @property
    def max_suggestions(self):
        return self.__max_suggestions

    @max_suggestions.setter
    def max_suggestions(self, new_max_suggestions: int):
        self.__max_suggestions = new_max_suggestions

    @abstractmethod
    def search(self, prefix: str) -> list[str]:
        raise NotImplementedError("Subclass should implement this!")
