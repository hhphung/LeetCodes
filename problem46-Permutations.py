class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if (len(nums) == 1):
            return [nums]

        for i in nums:
            new =[]
            for e in nums:
                new.append(e)
            new.remove(i)
            list = self.permute(new)

            for j in list:
                j.append(i)
            result.extend(list)


        return result
        
