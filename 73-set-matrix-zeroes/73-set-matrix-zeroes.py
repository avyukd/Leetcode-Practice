class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # pass 1 - collect 0 positions
        # pass 2 - modify rows and columns
        rows, columns = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        
        for r in rows:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
        
        for c in columns:
            for i in range(len(matrix)):
                matrix[i][c] = 0
        