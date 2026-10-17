# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res=[]
        ans=[]
        if root==None:
            return res
        def check(node,value):
            nonlocal ans,res
            if node==None:
                return 
            if node.left==None and node.right==None:
                if value==node.val:
                    ans.append(node.val)
                    res.append(ans.copy())
                    ans.pop()
                return
            ans.append(node.val)

            left=check(node.left,value-node.val)
            right=check(node.right,value-node.val)
            if ans:
                ans.pop()
        check(root,targetSum)
        return res