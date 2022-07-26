class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min= float('inf')
        result = 0
        for i in prices:
            if i < min:
                min = i
            if (i - min) > result:
                result = i - min
        return result
