class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        path = [[float('inf')] * (c+1) for x in range(r+1)]
        path[r-1][c] = 0
        for i in range(r -1,-1,-1): #col
            for j in range(c -1,-1,-1): #row
                path[i][j] = grid[i][j] + min(path[i+1][j], path[i][j+1])


        return path[0][0]
