class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        left = 0
        right = len(matrix[0])
        top = 0
        bot = len(matrix)
        while left < right and top < bot:
            for i in range (left, right):
                result.append(matrix[top][i])
            top+=1
            for i in range(top, bot):
                result.append(matrix[i][right-1])
            right-=1
            if not (left < right and top < bot):
                break

            for i in range(right-1, left-1, -1):
                result.append(matrix[bot-1][i])
            bot-=1
            for i in range(bot-1, top-1,-1):
                result.append(matrix[i][left])
            left+=1

        return result
