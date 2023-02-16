from .engines.BaseSearchEngine import BaseSearchEngine

class Autocomplete:
    def __init__(self, engine: BaseSearchEngine):
        self.engine = engine

    def suggestions_to(self, prefix: str):
        return self.engine.search(prefix.lower())

if __name__ == "__main__":
    from .engines.LinearSearchEngine import LinearSearchEngine
    from .utils.Dictionary import Dictionary

    import os 

    filename = os.path.join(os.getcwd(), "dictionary.txt")

    dictionary = Dictionary.from_file(filename)

    linearEngine = LinearSearchEngine(dictionary)

    autocomplete = Autocomplete(linearEngine)

    print(autocomplete.suggestions_to("brasi"))
