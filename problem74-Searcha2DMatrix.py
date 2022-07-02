class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        search = []
        for i in range(len(matrix)):
            if target <=matrix[i][len(matrix[0]) -1]:
                search = matrix[i]
                break
        low = 0
        high = len(search) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2

           
            if search[mid] < target:
                low = mid + 1

            
            elif search[mid] > target:
                high = mid - 1

            else:
                return True

        return False
