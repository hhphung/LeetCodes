class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i = 0
        result = []
        while i <= n:
            c = bin(i)[2:]
            add = self.hammingWeight(c)
            result.append(add)

            i+=1

        return result


    def hammingWeight(self, n):
        result = 0
        for i in n:
            if i == '1':
                result+=1
        return result
