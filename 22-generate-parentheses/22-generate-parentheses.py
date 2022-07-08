class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(comb, left, right):
            if len(comb) == 2 * n:
                result.append(comb[:])
                return
            if left < n:
                backtrack(comb+"(", left + 1, right)
            if right < left:
                backtrack(comb+")", left, right + 1)
        backtrack("", 0, 0)
        return result
                