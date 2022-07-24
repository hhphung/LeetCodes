class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for at in matrix:
            l = 0
            r = len(at)-1

            while l <= r:
                mid = l + (r - l) // 2
                if at[mid] == target:
                    return True
                elif at[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
