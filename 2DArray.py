#240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #no array -> false
        if len(matrix) == 0: return False
        # row from the bottom
        # column from the left
        row ,column = len(matrix)-1,0
        # while row reach top
        #while column reach right
        while row >=0 and column <len(matrix[0]):
            if matrix[row][column] == target:
                return True
            else:
                #target is larger than left and above
                if matrix[row][column] < target:
                    column += 1
                else:
                    row -= 1
        return False
