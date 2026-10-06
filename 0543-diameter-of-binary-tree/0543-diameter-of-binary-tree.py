class Solution(object):
    def diameterOfBinaryTree(self, root):
        maxi = 0

        def dfs(root):
            nonlocal maxi

            if root == None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            maxi = max(maxi, left + right)

            return 1 + max(left, right)

        dfs(root)
        return maxi