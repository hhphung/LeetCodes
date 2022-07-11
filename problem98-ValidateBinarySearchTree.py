class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dp(at, l, r):
            if not at:
                return True

            if not (at.val < r and at.val > l):
                return False
            return (dp(at.left, l, at.val) and
                    dp(at.right, at.val, r))


        return dp(root, float("-inf"), float("inf"))
