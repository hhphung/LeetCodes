class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        result = []
        for i in nums:
            if i in map:
                map[i] +=1
            else:
                map[i] =1
        for i in range(0,k):
            m = 0
            a = 0
            for j in map:
                if map[j] > m:
                    a = j
                    m = map[j]
            result.append(a)
            del map[a]
        return result
        
