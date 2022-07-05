class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if k >len(nums):
            k=k%len(nums)


        left =nums[0:len(nums)-k]
        right= nums[len(nums)-k:len(nums)]
        i =0
        for r in right:
            nums[i]= r
            i+=1
        for l in left:
            nums[i] = l
            i+=1
        return nums
