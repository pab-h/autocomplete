from .BaseSearchEngine import BaseSearchEngine

class LinearSearchEngine(BaseSearchEngine):
    def search(self, prefix: str) -> list[str]:
        suggestions: list[str] = []

        for word in self.dictionary():
            if word.startswith(prefix):
                suggestions.append(word)

            if len(suggestions) == self.max_suggestions:
                break

        return suggestions

if __name__ == "__main__":
    from ..utils import Dictionary
    import os


    filename = os.path.join(os.getcwd(), "dictionary.txt")

    dictionary = Dictionary(filename)

    linearSearch = LinearSearchEngine(dictionary)
    linearSearch.max_suggestions = 5
    
    suggestions = linearSearch.search("brasi")

    print(suggestions)