class Solution(object):
    def searchInsert(self, nums, target):
        result = 0
        less = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target > nums[i]:
                less = i +1

        return less
        
