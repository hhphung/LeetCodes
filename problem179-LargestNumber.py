from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def strNumCompare(s1, s2):
            i, length = 0, len(s1) + len(s2)
            s1, s2 = s1 + s2, s2 + s1
            while i < length:
                if s1[i] != s2[i]:
                    return ord(s1[i]) - ord(s2[i])
                i += 1
            return 0

        nums = sorted(map(str, nums), key=cmp_to_key(strNumCompare), reverse=True)
        ans = ''.join(nums).lstrip('0')
        return ans if ans else '0'
