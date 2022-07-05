class Solution(object):
    def rob(self, nums):
        first = 0
        second = 0

        for i in nums:
            t = max(i+first, second)
            first = second
            second=t
        return second
