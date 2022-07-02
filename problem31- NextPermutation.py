class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        last = len(nums) - 1
        if len(nums) <=1:
            return nums
        while last >=0:
            if nums[last] > nums[last-1] or last == 0:
                break
            last-=1

        if last != 0:
            pivot = last-1
            i = len(nums)-1

            while nums[pivot] >= nums[i]:
                i-=1
            temp = nums[i]
            nums[i] = nums[pivot]
            nums[pivot] = temp


        nums[last:len(nums)] = sorted(nums[last:len(nums)])

        return nums
