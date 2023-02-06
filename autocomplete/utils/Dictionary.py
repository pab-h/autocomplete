class Dictionary:
    @staticmethod
    def saniteze(words: list[str]):
        return [word.split('\n')[0] for word in words]

    def __init__(self, path: str) -> None: 
        self.__words = self.__load(path)

    def __call__(self):
        return self.__words

    def __load(self, path: str) -> list[str]:
        with open(path, 'r') as file:
            words = file.readlines()
            
            return Dictionary.saniteze(words)

if __name__ == '__main__':
    import os

    dictionary_filename = "dictionary.txt"

    path = os.path.join(
        os.getcwd(), 
        dictionary_filename
    )

    dictionary = Dictionary(path)
    print(dictionary())