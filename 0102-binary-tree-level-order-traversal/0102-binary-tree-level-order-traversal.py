# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,root,level,result):
        if root==None:
            return
        if len(result)==level:
            result.append([])
        result[level].append(root.val)
        self.dfs(root.left,level+1,result)
        self.dfs(root.right,level+1,result)

    def levelOrder(self, root):
        result=[]
        if root==None:
            return result
        self.dfs(root,0,result)
        return result

        