class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result =[]
        if len(nums) <4:
            return result
        list = sorted(nums)
        size = len(nums)
        for i in range(len(list)-3):
            for j in range(i+1, len(list)-2):
                left = j+1
                right = size-1
                n = (target-(list[i] + list[j]))
                while left  < right:
                    sum = list[left] + list[right]
                    if sum > n:
                        right -= 1
                    elif sum <n:
                        left += 1
                    else:
                        a = list[i],list[j], list[left], list[right]
                        if a not in result:
                            result.append(a)
                        left += 1
                        right -= 1
        return result
        
