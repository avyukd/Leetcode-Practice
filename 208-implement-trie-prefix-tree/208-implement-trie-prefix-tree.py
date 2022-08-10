class Node:
    def __init__(self):
        self.children = [None] * 26
        self.eow = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        head = self.root
        for i in range(len(word)):
            nxt = head.children[ord(word[i]) - ord('a')]
            if nxt is None:
                nxt = Node()
                head.children[ord(word[i]) - ord('a')] = nxt
            head = head.children[ord(word[i]) - ord('a')] 
        head.eow = True
        
    def search(self, word: str) -> bool:
        head = self.root
        i = 0
        while i < len(word):
            head = head.children[ord(word[i]) - ord('a')]
            if head:
                i += 1
            else:
                break
        return i == len(word) and head.eow
            
    def startsWith(self, prefix: str) -> bool:
        head = self.root
        i = 0
        while i < len(prefix):
            head = head.children[ord(prefix[i]) - ord('a')]
            if head:
                i += 1
            else:
                break
        return i == len(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)