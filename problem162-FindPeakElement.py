class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peak = 0
        i =1
        while i <len(nums):
            k = len(nums)
            if i == len(nums)-1 and nums[i-1] < nums[i]:
                peak = i
            elif nums[i-1] < nums[i] and nums[i+1]<nums[i]:
                peak = i
            i+=1
        return peak
