import os
from pathlib import Path

class Dictionary:
    @staticmethod
    def clean_words(words: list[str]):
        return [word.split('\n')[0] for word in words]

    def __init__(self, path: str) -> None: 
        self.__words = self.__load(path)

    def __load(self, path: str) -> list[str]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File { path } not found")

        with open(path, 'r') as file:
            words = file.readlines()
            
            return Dictionary.clean_words(words)

    def update_path(self, path: str):
        self.__words = self.__load(path)

    @property
    def words(self): 
        return self.__words

if __name__ == '__main__':
    dictionary_filename = "dictionary.txt"

    path = os.path.join(
        Path.cwd(), 
        dictionary_filename
    )

    dictionary = Dictionary(path)
    print(dictionary.words)