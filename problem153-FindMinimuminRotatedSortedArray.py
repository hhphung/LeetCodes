class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=1:
            return nums[0]

        mid = (len(nums))//2
        arr = nums[0:mid]
        if arr[-1] > nums[-1]:
            arr = nums[mid:len(nums)]

        m = float('inf')
        for i in arr:
            m = min(m, i)
        return m
        
