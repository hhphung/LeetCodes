class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * (n)

        for i in range(0, n):
            for prev in range(0, i):
                if nums[i] > nums[prev]:
                    dp[i] = max(dp[i], 1 + dp[prev])
        ans = max(dp)
        return ans
