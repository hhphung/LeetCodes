class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g', 'h', 'i'],
            '5': ['j','k','l'],
            '6': ['m','n', 'o'],
            '7': ['p','q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ans = []
        for i in digits:
            if len(ans) == 0:
                ans.extend(dic[i])
            else:
                ans = [ans[j] + x for x in dic[i] for j in range(len(ans))]
        return ans
        
