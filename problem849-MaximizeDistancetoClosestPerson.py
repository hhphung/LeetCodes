class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 1

        for i in range(len(s) -1):
            j = i +1
            string = s[i]
            while j <len(s):
                if s[j] not in string:
                    string += s[j]
                else:
                    sum = max(sum, (len(string)))
                    break
                j+=1
        return sum
