class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) -1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                continue
            i+=1
        return len(nums)
