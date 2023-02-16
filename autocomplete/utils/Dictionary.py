class Dictionary:
    @staticmethod
    def format(words: list[str]):
        return [word.split('\n')[0].lower() for word in words]

    def __init__(self, words: list[str]) -> None: 
        self.words = words
    
    @classmethod
    def from_file(cls, path: str):
        with open(path, 'r') as file:
            words = file.readlines()

            return cls(cls.format(words))

if __name__ == '__main__':
    import os

    dictionary_filename = "dictionary.txt"

    path = os.path.join(
        os.getcwd(), 
        dictionary_filename
    )

    dictionary = Dictionary.from_file(dictionary_filename)
    print(dictionary.words)