class Solution(object):
    def maxSubArray(self, nums):
        max = 0
        sum = nums[0]
        for i in nums:
            max+=i
            if sum < max:
                sum = max
            if max <=0:
                max = 0
        return sum
