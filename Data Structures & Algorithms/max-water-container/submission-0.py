class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxval = 0

        while l < r:
            width = r-l
            height = min([heights[l], heights[r]])
            area = width*height
            if area > maxval:
                maxval = area
            if heights[l] < heights[r]:
                l = l+1
            else:
                r = r-1
        
        return maxval