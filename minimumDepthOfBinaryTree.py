# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
       
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + min([self.minDepth(x) for x in (root.left, root.right) if x] or [0])