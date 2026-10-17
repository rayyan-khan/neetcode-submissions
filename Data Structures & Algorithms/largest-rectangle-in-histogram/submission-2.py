class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_limits = [-1] * n
        right_limits = [n] * n
        
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_limits[i] = stack[-1]
            stack.append(i)
            
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_limits[i] = stack[-1]
            stack.append(i)
            
        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (right_limits[i] - left_limits[i] - 1))
            
        return max_area