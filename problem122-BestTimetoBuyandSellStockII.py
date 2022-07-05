class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        i = len(prices) -1
        while i  >= 0:
            if i == 0:
                break
            if prices[i] > prices[i-1]:
                largest = prices[i]
                i-=1

                while  i-1 >= 0 and prices[i] > prices[i-1]:
                    i-=1
                result +=largest - prices[i]
            else:
                i-=1
        return result
