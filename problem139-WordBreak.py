class Solution(object):
    def wordBreak(self, s, wordDict):
        lookup = {"": True}
        def dp(string, wordDict):
            if string in lookup:
                return lookup[string]
            for i in range(len(string)):
                if string[:i+1] in wordDict:
                    x = dp(string[i+1:], wordDict)
                    lookup[string[i+1:]] = x
                    if x:
                        return True
            return False
        return dp(s, wordDict)
