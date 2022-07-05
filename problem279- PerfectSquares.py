class Solution(object):
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        currs = [n]
        count = 0
        seen = set()
        while currs:
            nxts = []
            for curr in currs:
                for square_num in squares:
                    left_num = curr-square_num
                    if left_num in seen:
                        continue
                    if left_num<0:
                        break
                    if left_num > 0:
                        seen.add(left_num)
                        nxts.append(left_num)
                    else:
                        return count+1
            currs = nxts
            count += 1
