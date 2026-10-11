# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        dia=0
        lr_max=0
        if root==None:
            return 0
        def check(node):
            nonlocal dia,lr_max

            if node==None:
                return 0
            left=check(node.left)
            right=check(node.right)
            lr_max=max(left,right)
            dia=max(dia,lr_max)
            return 1+max(left,right)
        check(root)
        return lr_max+1
