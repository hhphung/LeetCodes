class Solution(object):
    def isPalindrome(self, x):
        String = str(x)
        reverse = String [::-1]
        return String == reverse
