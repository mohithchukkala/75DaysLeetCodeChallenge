# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def som(self,root,ans):
        if root==None:
            return 
        self.som(root.left,ans)
        ans.append(root.val)
        self.som(root.right,ans)
    def inorderTraversal(self, root):
        ans=[]
        self.som(root,ans)
        return ans
        