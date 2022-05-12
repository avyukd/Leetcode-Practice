class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        i,j = 0,0
        state = "R"
        while True:
            spiral.append(matrix[i][j])
            matrix[i][j] = -101
            if state == "R":
                if (j + 1) < len(matrix[0]) and matrix[i][j + 1] != -101:
                    j += 1
                elif (i + 1) < len(matrix) and matrix[i+1][j] != -101:
                    state = "D"
                    i += 1
                else:
                    break
            elif state == "D":
                if (i + 1) < len(matrix) and matrix[i + 1][j] != -101:
                    i += 1
                elif (j - 1) >= 0 and matrix[i][j - 1] != -101:
                    state = "L"
                    j -= 1
                else:
                    break
            elif state == "L":
                if (j - 1) >= 0 and matrix[i][j - 1] != -101:
                    j -= 1
                elif (i - 1) >= 0 and matrix[i - 1][j] != -101:
                    state = "U"
                    i -= 1
                else: 
                    break
            else:
                # state up
                if (i - 1) >= 0 and matrix[i - 1][j] != -101:
                    i -= 1
                elif (j + 1) < len(matrix) and matrix[i][j + 1] != -101:
                    state = "R"
                    j += 1
                else: 
                    break
        return spiral