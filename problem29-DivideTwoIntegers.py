class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        d = abs(dividend)
        r = abs(divisor)
        while(d >= r):
            gr = r
            ins = 1
            while(d >= gr):
                d -= gr
                result+=ins
                gr+=gr
                ins+=ins

        if(dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor <0):
            result = abs(result)
        else:
            result = -result

        if(result > math.pow(2,31) -1):
            result= int (math.pow(2,31) -1)
        elif (result < -(math.pow(2,31))):
            result =  int(math.pow(2,31))

        return result
