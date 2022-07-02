class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = defaultdict(list)
        for i in strs:
            count = [0]* 26;
            for j in i:
                count [ord(j) - ord("a")] +=1
            result[tuple(count)].append(i)

        return result.values()
