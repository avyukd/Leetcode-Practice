class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        abbr = defaultdict(set)
        for word in dictionary:
            abbr[self.abbreviate(word)].add(word)
        self.abbr = abbr
        
    def isUnique(self, word: str) -> bool:
        curr = self.abbreviate(word)
        if curr in self.abbr:
            return word in self.abbr[curr] and len(self.abbr[curr]) == 1 
        else:
            return True
    
    def abbreviate(self, word):
        return word if len(word) == 1 else (word[0] + (str(len(word) - 2) if len(word) > 2 else "") + word[-1])

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)