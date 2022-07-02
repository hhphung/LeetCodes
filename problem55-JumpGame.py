class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = False
        goal = len(nums)-1
        i = len(nums)-1
        while i >= 0:
            if i + nums[i] >= goal:
                goal = i
            i-=1

        if goal == 0:
            result = True

        return result
