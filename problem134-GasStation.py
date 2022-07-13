class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        dif = []
        s = 0
        result = 0
        for i in range(len(gas)):
            dif.append(gas[i] - cost[i])
        for j in range(len(dif)):
            s += dif[j]
            if s < 0:
                s = 0
                result= j+1


        return result
