import copy


class Solution(object):
    def combinationSum(self, candidates, target):

        result=[]
        def backTracking(a,b,total):
            if total == target:
                result.append(copy.deepcopy(b))
                return 
            if a >= len(candidates) or total > target:
                return
            b.append(candidates[a])
            backTracking(a, b, total+ candidates[a])
            b.pop()
            backTracking(a+1, b, total)
        backTracking(0,[],0)

        return result
