class Solution(object):
    def isValid(self, s):
        array = []
        for sym in s:
            if sym == '(' or sym == '[' or sym == '{':
                array.append(sym)
            else:
                if sym ==')':
                    if len(array) < 1:
                        return False
                    elif array[-1] != '(':
                        return False
                    else:
                        array.pop(-1)
                elif sym == ']':
                    if len(array) < 1:
                        return False
                    elif array[-1] != '[':
                        return False
                    else:
                        array.pop(-1)
                elif sym == '}':
                    if len(array) < 1:
                        return False
                    elif array[-1] != '{':
                        return False
                    else:
                        array.pop(-1)
        if len(array) > 0:
            return False

        return True
