class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        output = ""
        compare = min(strs, key = len)
        for i in range(len(compare)):
            if all([x.startswith(compare[:i+1]) for x in strs]):
                    output = compare[:i+1]
            else:
                    break
        return output
