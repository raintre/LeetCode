# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            return t2
        if t1 and not t2:
            return t1
        if not t1 and not t2:
            return

        newTree = TreeNode(t1.val + t2.val)
        newTree.left = self.mergeTrees(t1.left, t2.left)
        newTree.right = self.mergeTrees(t1.right, t2.right)

        return newTree
