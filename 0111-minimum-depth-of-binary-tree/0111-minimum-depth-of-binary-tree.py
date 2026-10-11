# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        dia=-100000
        lr_min=0
        if root==None:
            return 0
        def check(node):
            nonlocal dia,lr_min
            if node==None:
                return 0

            left=check(node.left)
            right=check(node.right)
            if left==0:
                return 1+right
            elif right==0:
                return 1+left
            else:
                return 1+min(left,right)

        return check(root)
