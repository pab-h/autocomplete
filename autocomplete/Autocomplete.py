from .engines.BaseSearchEngine import BaseSearchEngine

class Autocomplete:
    def __init__(self, engine: BaseSearchEngine):
        self.__engine = engine

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, other_engine: BaseSearchEngine):
        self.__engine = other_engine

    def suggestions_to(self, prefix: str):
        return self.__engine.search(prefix)

if __name__ == "__main__":
    from .engines.LinearSearchEngine import LinearSearchEngine
    from .utils.Dictionary import Dictionary

    import os 

    filename = os.path.join(os.getcwd(), "dictionary.txt")

    dictionary = Dictionary(filename)

    linearEngine = LinearSearchEngine(dictionary)

    autocomplete = Autocomplete(linearEngine)

    print(autocomplete.suggestions_to("brasi"))
