import copy
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.stack  = nums
        self.ori = copy.deepcopy(nums)

    def reset(self):
        """
        :rtype: List[int]
        """
        self.stack[:] = self.ori
        return self.stack

    def shuffle(self):
        """
        :rtype: List[int]
        """
        random.shuffle(self.stack)
        return self.stack
