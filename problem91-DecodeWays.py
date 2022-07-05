class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic ={ len(s):1}
        def search(k):
            if k in dic:
                return dic[k]
            if s[k] == "0":
                return 0
            result = search(k+1)
            if (k+1 < len(s) and (s[k] =="1" or s[k] =="2" and s[k+1] in "0123456")):
                result+= search(k+2)
            dic[k] = result
            return result

        return search(0)
