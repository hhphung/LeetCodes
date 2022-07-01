import math

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {
            1:'I',
            4:'IV',
            9: 'IX',
            5:'V',
            10:'X',
            40: 'XL',
            50:'L',
            90: 'XC',
            100:'C',
            400: 'CD',
            500:'D',
            900: 'CM',
            1000: 'M'
        }
        mul =10
        result = ""
        if num in dic:
            return dic[num]
        while num > 0:
            s = num % mul
            add = ""
            x = s
            while x not in dic and x > 0:
                n = mul//10
                add+=dic[n]
                x-=n
            if x != 0:
                add = dic[x] +add
            result = add + result
            num-=s
            mul *= 10
        return result
