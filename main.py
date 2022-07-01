import copy


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        part =[]
        def search(i):
            if i >= len(s):
                result.append(copy.deepcopy(part))
                return
            for k in range(i, len(s)):
                if self.isPalindrome(s[i:k+1]):
                    part.append(s[i:k+1])
                    search(k+1)
                    part.pop()
        search(0)
        return result

    def isPalindrome(self,s):
        return s == s[::-1]












