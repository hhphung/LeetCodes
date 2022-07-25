class Solution(object):
    def productExceptSelf(self, nums):
        prefix = 1
        ans = []
        for ele in nums:
            ans.append(prefix)
            prefix *= ele
        prefix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= prefix
            prefix *=nums[i]
        return ans
