class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col  = [1]*len(matrix)
        row = [1]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    col[i] = 0
                    row[j] = 0
        for i in range(len(col)):
            if col[i] == 0:
                for j in range(len(row)):
                    matrix[i][j] = 0
        for j in range(len(row)):
            if row[j] == 0 :
                for i in range(len(col)):
                    matrix[i][j] = 0

        return matrix
