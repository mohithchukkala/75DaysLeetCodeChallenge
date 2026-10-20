# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        if root==None:
            return False
        queue=deque([(root,None)])
        while queue:
            x_parent=None
            y_parent=None
            for i in range(len(queue)):
                node,parent=queue.popleft()
                if node.val==x:
                    x_parent=parent
                if node.val==y:
                    y_parent=parent
                if node.left:
                    queue.append((node.left,node))
                if node.right:
                    queue.append((node.right,node))
            if x_parent is not None and y_parent is not None:
                if x_parent!=y_parent:
                    return True
        
                
        return False
          
            