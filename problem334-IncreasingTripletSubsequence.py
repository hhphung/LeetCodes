class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result =[float('inf')]*3

        for i in nums:
            for j in range(len(result)):
                if i <= result[j]:
                    if (j == 2):
                        return True
                    result[j] = i
                    break


        return False
