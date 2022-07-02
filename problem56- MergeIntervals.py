class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        new_list =sorted(intervals, key = lambda  x: (x[0]))
        i = 0
        while i < len(new_list)-1:
            if new_list[i][1] >= new_list[i+1][0]:
                new = [min(new_list[i][0], new_list[i+1][0]), max(new_list[i][1], new_list[i+1][1])]
                new_list.remove(new_list[i])
                new_list.remove(new_list[i])
                new_list.insert(i,new)

            else:
                i+=1

        return new_list
