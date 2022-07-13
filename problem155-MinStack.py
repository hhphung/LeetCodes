class MinStack(object):

    def __init__(self):
        self.stack = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        m = val
        if self.stack:
            m = min(m, self.stack[-1][1])
        self.stack.append([val, m])


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
