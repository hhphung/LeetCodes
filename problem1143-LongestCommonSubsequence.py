class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """



        result =  [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    result[i][j]= 1+ result[i+1][j+1]
                else:
                    result[i][j] = max(result[i][j+1], result[i+1][j])



        return result[0][0]
