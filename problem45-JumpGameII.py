class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length= len(nums) - 1
        curr =  -1
        nxt= 0
        ans=0
        i = 0
        while nxt < length:
            if i > curr:
                ans += 1
                curr = nxt
            nxt = max(nxt, nums[i] + i)
            i += 1
        return ans
