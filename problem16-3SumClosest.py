class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result =-1000
        list=sorted(nums)
        for i in range(len(list)-2):
            left = i+1
            right = len(nums)-1
            while left <right:
                n = list[i] + list[left] + list[right]
                if  abs(target-result) > abs(target-n) or n == target:
                    result = n
                    if  n > target:
                        right -= 1
                    else:
                        left += 1
                elif n > target:
                    right -= 1
                else:
                    left += 1
        return result
