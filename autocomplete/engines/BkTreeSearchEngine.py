from .BaseSearchEngine import BaseSearchEngine

from ..utils import Dictionary
from ..utils import BKTree
from ..utils import distance_function_type
from ..utils import levenshtein_distance

class BkTreeSearchEngine(BaseSearchEngine):
    def __init__(self, dictionary: Dictionary, tolerance: int = 1, d: distance_function_type = levenshtein_distance) -> None:
        super().__init__(dictionary)

        self.bktree = BKTree(d)

        self.tolerance = tolerance

        for word in self.dictionary.words:
            self.bktree.insert(word)

    def search(self, prefix: str) -> list[str]:
        result = map(
            lambda node: node.word, 
            self.bktree.search(prefix, self.tolerance)
        )

        return list(result)[: self.max_suggestions]