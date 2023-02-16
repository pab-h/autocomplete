from .BaseSearchEngine import BaseSearchEngine

from ..utils import Dictionary
from ..utils.Trie import Trie

class TrieSearchEngine(BaseSearchEngine):
    def __init__(self, dictionary: Dictionary) -> None:
        super().__init__(dictionary)

        self.trie = Trie()

        for word in self.dictionary.words:
            self.trie.insert(word)

    def search(self, prefix: str) -> list[str]:
        return self.trie.search(prefix)[: self.max_suggestions]

if __name__ == "__main__":
    dictionary = Dictionary(["o", "ol", "olá"])

    print(dictionary.words)

    engine = TrieSearchEngine(dictionary)

    print(engine.search("ol"))