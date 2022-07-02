import math
class Solution(object):
    def searchRange(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                i = mid - 1
                j = mid + 1
                while nums[i] == target and i >= 0:
                    i -= 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                return [i + 1, j - 1]
        return [-1,-1]
