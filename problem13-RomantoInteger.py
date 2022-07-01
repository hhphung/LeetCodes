class Solution(object):
  def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int = 0
        s= str(s)
        for i in range(len(s)):
            if i+ 1 != len(s):
                if roman[s[i]] >= roman[s[i + 1]]:
                    int += roman[s[i]]
                else:
                    int -= roman[s[i]]
            else:
                int += roman[s[i]]

        return int
