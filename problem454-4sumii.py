import math


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """


        first = {}

        result = 0
        for a in nums1:
            for b in nums2:
                if a+b in first:
                    first[a+b]+=1
                else:
                    first[a+b] =1
        for c in nums3:
            for d in nums4:
                target = -(c+d)
                if target in first:
                    result+=first[target]
        return result
