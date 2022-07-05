class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return 0
        result = self.factorial(n)
        x = self.end_zeros(result)
        return x

    def end_zeros(self,num):
        new_num = str(num)
        count = len(new_num) - len(new_num.rstrip("0"))
        return count
    def factorial(self,n):
        if n ==0:
            return 0
        if n==1:
            return 1
        else:
            return n*self.factorial(n-1)
