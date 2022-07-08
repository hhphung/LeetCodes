class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        num = 9
        while num > 0:
            stack = set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == str(num):
                        if not self.valid(stack, (i, j)):
                            return False
                        stack.add((i, j))
            num -= 1
            for x in range(0, len(board), +3):
                for y in range(0, len(board), +3):
                    lst = []
                    for i in range(3):
                        for j in range(3):

                            if board[i + x][j + y] == ".": continue
                            if board[i + x][j + y] in lst: return False
                            lst.append(board[i + x][j + y])
        return True

    def valid(self, set, x):
        for i in set:
            if i[0] == x[0] or i[1] == x[1]:
                return False

        return True
