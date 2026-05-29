class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node:
            return None

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            copy = Node(node.val)
            visited[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)