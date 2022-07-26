class Solution(object):
    def climbStairs(self, n):
        first = 1
        second = 1
        for i in range(2, n + 1):
            second, first = first + second, second
        return second
