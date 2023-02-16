class TrieNode:
    def __init__(self, value: str) -> None:
        self.value = value
        
        self.is_end = False

        self.children: dict[str, TrieNode] = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")

    def insert(self, word: str):
        current = self.root

        for char in word:
            children = current.children.get(char)

            if not children:
                children = TrieNode(char)

            current.children.update({ char: children })

            current = children

        current.is_end = True

    def start_with(self, preffix: str):
        current = self.root
        
        for char in preffix:
            children = current.children.get(char)

            if not children:
                return False

            current = children

        return True

    def get_words(self, words: list[str], node: TrieNode | None = None, word_part = ""):
        if node is None:
            node = self.root

        word = word_part + node.value

        if node.is_end:
            words.append(word)

        for child in node.children.values():
            self.get_words(words, child, word)

    def search(self, prefix: str):
        if not self.start_with(prefix):
            return list[str]()

        current = self.root 

        for char in prefix:
            current = current.children[char]           

        words: list[str] = []

        self.get_words(words, current, prefix[:-1])

        return words

if __name__ == "__main__":
    trie = Trie()

    trie.insert("arroz")
    trie.insert("arroto")

    print(trie.search(""))

