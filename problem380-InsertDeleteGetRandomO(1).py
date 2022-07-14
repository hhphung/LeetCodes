import  random
class RandomizedSet(object):

    def __init__(self):
        self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not (val in self.list):
            self.list.append(val)
            return True
        return False


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.list:
            self.list.remove(val)
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        a = random.randrange(0, len(self.list))
        return self.list[a]
