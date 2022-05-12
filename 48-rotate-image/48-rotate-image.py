class Solution:
    # alternatively: could do transpose + reverse solution, worth trying out later
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose():
            for i in range(len(matrix)):
                for j in range(i+1, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        def reflect():
            for i in range(len(matrix)):
                for j in range(len(matrix) // 2):
                    matrix[i][j], matrix[i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j], matrix[i][j]
        
        transpose()
        reflect()
    # swap groups of 4 cells
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         # intuition: rotate groups of 4 moving inwards
#         # 1. get num of levels to move inwards
#         levels = len(matrix) // 2 # if even, / 2. if odd, / 2 floor
        
#         for level in range(levels):
#             for i in range(len(matrix) - 2 * level - 1):
#                 # get group of 4 corners
#                 corner1 = (level, level + i)
#                 corner2 = (level + i, len(matrix) - 1 - level)
#                 corner3 = (len(matrix) - 1 - level, len(matrix) - 1 - level - i)
#                 corner4 = (len(matrix) - 1 - level - i, level)
#                 # swap the corners accordingly
#                 tmp = matrix[corner1[0]][corner1[1]]
#                 matrix[corner1[0]][corner1[1]] = matrix[corner4[0]][corner4[1]]
#                 matrix[corner4[0]][corner4[1]] = matrix[corner3[0]][corner3[1]]
#                 matrix[corner3[0]][corner3[1]] = matrix[corner2[0]][corner2[1]]
#                 matrix[corner2[0]][corner2[1]] = tmp
        
        