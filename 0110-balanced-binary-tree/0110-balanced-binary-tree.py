# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        dia=0
        def check(node):
            nonlocal dia
            if node==None:
                return 0
            left=check(node.left)
            right=check(node.right)
            if left==-1 or right==-1:
                return -1
            if abs(right-left)>1:
                return -1
            return 1+max(left,right)
        return check(root)!=-1