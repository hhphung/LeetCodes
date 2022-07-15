class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        list = []
        for i in matrix:
            list.extend(i)
        list.sort()
        return list[k-1]
