class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result  =0
        if len(s) < k:
            return 0
        strings = []
        list = {}
        at = 0
        for i in s:
            if i in list:
                list[i] +=1
            else:
                list[i] = 1
        same = True
        for a in list:
            if list[a] < k:
                same = False
        if same:
            return len(s)
        while len(s) > 0:
            if list[s[at]] < k:
                m = s[0:at]
                if len(m) > 0:
                    strings.append(m)
                s =  s[at+1: len(s)]
                at= 0
            elif at == len(s)-1:
                strings.append(s)
                break
            else:
                at+=1

        for i in strings:
            result = max(self.longestSubstring(i,k),result)
        return result
