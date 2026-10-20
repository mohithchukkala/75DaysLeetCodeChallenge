# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        res=[]
        if root==None:
            return res

        queue=deque([root])
        while queue:
            popi=queue.pop()
            res.append(popi.val)
            queue.append(popi)
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
            