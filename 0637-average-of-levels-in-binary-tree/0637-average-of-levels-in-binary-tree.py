# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if root==None:
            return 0
        res=[]
        queue=deque([root])
        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans=0
            for i in range(len(level)):
                ans+=level[i]
            res.append(ans/len(level))
        return res
        

        