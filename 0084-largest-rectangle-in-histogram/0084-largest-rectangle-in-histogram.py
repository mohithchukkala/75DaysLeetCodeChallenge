class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # will store indices
        max_area = 0
        heights.append(0)  # sentinel to empty stack at end

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                
                # if stack empty → width = i
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
