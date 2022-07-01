class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) -1
        result = 0
        while left < right:
            area = (right - left)*min(height[left], height[right])
            result =  max(result,area )
            if height[left] > height[right]:
                right-=1
            elif height[right] > height[left]:
                left+=1
            else:
                left+=1
                right-=1
        return result
