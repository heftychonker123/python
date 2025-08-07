class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary mapping characters to TrieNode
        self.is_end = False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        current=self.root
        for c in word:
            if c not in current.children:
                current.children[c]=TrieNode()
            current=current.children[c]
        current.is_end=True
    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        count = 1  # Count this node
        for child in node.children.values():
            count += self._count_nodes(child)
        return count
    def print_structure(self, node=None, prefix="", level=0):
        if node is None:
            node = self.root
        for char, child in node.children.items():
            print("  " * level + "|-- " + char)
            self.print_structure(child, prefix + char, level + 1)

n=int(input())
trie=Trie()
for _ in range(n):
    tel=input()
    trie.insert(tel)
trie.print_structure()
print(trie.count_nodes()-1)
