# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        result =self.BST_to_array(root)

        return result[k-1]

    def BST_to_array(self, root):
        if root:
            return self.BST_to_array(root.left) + [root.val] + self.BST_to_array(root.right)
        else:
            return []
