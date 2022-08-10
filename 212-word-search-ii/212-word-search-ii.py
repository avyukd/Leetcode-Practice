class Node:
    def __init__(self):
        self.children = [None] * 26
        self.eow = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for i in range(len(word)):
            nxt = curr.children[ord(word[i]) - ord('a')]
            if nxt is None:
                curr.children[ord(word[i]) - ord('a')] = Node()
            curr = curr.children[ord(word[i]) - ord('a')]
        curr.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 0:
            return []
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        m, n = len(board), len(board[0])
        
        valid = set()
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(root, i, j, word, parent):
            if (i, j) not in visited:
                if root.eow:
                    valid.add(word)
                
                if all([child is None for child in root.children]):
                    # leaf node
                    key = ord(board[i][j]) - ord('a')
                    parent.children[key] = None
                
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        key = ord(board[ni][nj]) - ord('a')
                        if root.children[key] is not None:
                            visited.add((i, j))
                            dfs(root.children[key], ni, nj, word +
                                board[ni][nj], root)
                            visited.remove((i, j))
                
        for i in range(m):
            for j in range(n):
                key = ord(board[i][j]) - ord('a')
                if trie.root.children[key]:
                    visited = set()
                    dfs(trie.root.children[key], i, j, board[i][j], trie.root)
        
        return valid