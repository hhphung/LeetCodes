class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        array = s.split()
        s = array[-1]
        return len(s)
