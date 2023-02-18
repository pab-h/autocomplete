from .distance_functions import distance_function
from .distance_functions import levenshtein

class BKTreeNode: 
    def __init__(self, word: str) -> None:
        self.word = word
        
        self.children: dict[int, BKTreeNode] = {}

    def __repr__(self) -> str:
        return self.word

class BKTree:
    def __init__(self, d: distance_function = levenshtein, root: BKTreeNode | None = None) -> None:
        self.root = root
        
        self.d = d

    def insert(self, word: str):
        new = BKTreeNode(word)

        if self.root is None:
            self.root = new

            return

        current = self.root

        while True:
            distance = self.d(current.word, new.word)

            child = current.children.get(distance)

            if child is None:
                current.children.update({ distance: new })
                
                break

            current = child

    def search(self, word: str, tolerance: int):
        if self.root is None:
            raise ValueError("Bk Tree is empty")

        candidates = [self.root]

        found: list[BKTreeNode] = []

        while len(candidates) > 0:
            node = candidates.pop(0)

            distance = self.d(node.word, word)

            if distance <= tolerance:
                found.append(node)

            candidates.extend(child_node for child_distance, child_node in node.children.items() 
                                if distance - tolerance <= child_distance <= distance + tolerance)

        return found

if __name__ == "__main__":
    tree = BKTree()

    tree.insert("a")
    tree.insert("boa")
    tree.insert("boi")
    tree.insert("boiasd")
    tree.insert("boi23131231")

    print(tree.search("boai", 2))