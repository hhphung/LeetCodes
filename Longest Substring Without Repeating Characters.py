class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        set = {}
        result = 0
        while left < len(s):
            c = s[left]
            if c in set:
                left = set[c] +1
                set = {}
            else:
                set[c] = left
                left+=1
            result = max(result, len(set))
        return result

