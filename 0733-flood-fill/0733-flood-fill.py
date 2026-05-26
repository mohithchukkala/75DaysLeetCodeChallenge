class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        original = image[sr][sc]

        if original == color:
            return image

        def dfs(r, c):
            if (r < 0 or r >= len(image) or
                c < 0 or c >= len(image[0]) or
                image[r][c] != original):
                return

            image[r][c] = color

            dfs(r+1, c)   # down
            dfs(r-1, c)   # up
            dfs(r, c+1)   # right
            dfs(r, c-1)   # left

        dfs(sr, sc)
        return image