class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordToGenerics = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                wordToGenerics[word].append(word[:i] + "*" + word[i+1:])
        
        genericToWords = defaultdict(list)
        for key in wordToGenerics:
            for generic in wordToGenerics[key]:
                genericToWords[generic].append(key)
        
        queue = deque([beginWord])
        levels = 1
        visited = set()
        while queue:
            level = list(queue)
            queue = deque([])
            for node in level:
                if node not in visited:
                    visited.add(node)
                    if node == endWord:
                        return levels
                    genericForms = wordToGenerics[node]
                    for genericForm in genericForms:
                        for child in genericToWords[genericForm]:
                            queue.append(child)
            
            levels += 1
        return 0

# first attempt, too slow, no preprocessing
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
#         if endWord not in wordList:
#             return 0
        
#         def differsByOne(word1, word2):
#             if len(word1) != len(word2):
#                 return False
#             numDiffs = 0
#             for i in range(len(word1)):
#                 if word1[i] != word2[i]:
#                     numDiffs += 1
#                 if numDiffs > 1:
#                     return False
#             return numDiffs == 1
        
#         adj = defaultdict(list)
#         for word in wordList:
#             if differsByOne(beginWord, word):
#                 adj[beginWord].append(word)
        
#         queue = deque([beginWord])
#         visited = set()
#         levels = 1
#         while queue:
#             level = list(queue)
#             queue = deque([])
#             for node in level:
#                 if node not in visited:
#                     visited.add(node)
#                     if node == endWord:
#                         return levels
#                     for word in wordList:
#                         if differsByOne(node, word):
#                             adj[node].append(word)
#                             adj[word].append(node)
#                     for child in adj[node]:
#                         queue.append(child)
#             levels += 1
        
#         return 0