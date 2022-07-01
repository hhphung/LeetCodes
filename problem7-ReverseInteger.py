class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0

        if (x > 0):
            while (x > 0):
                i = x % 10
                rev = rev * 10 + i
                x = int(x / 10)
        else:
            x = x * -1
            while (x > 0):
                i = x % 10
                rev = rev * 10 + i
                x = int(x / 10)
            rev = rev * -1

        return rev if -(2 ** 31) - 1 < rev < 2 ** 31 else 0