class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # naive approach?
        areas = []

        for c in range(len(heights)):
            r, l = c + 1, c - 1
            width_for_col = 1
            if c == 0:  # extend right only
                while r < len(heights) and heights[r] >= heights[c]:
                    width_for_col += 1
                    r += 1
            elif c == len(heights) - 1:  # extend left only
                while l >= 0 and heights[l] >= heights[c]:
                    width_for_col += 1
                    l -= 1
            else:  # extend right and left
                while r < len(heights) and heights[r] >= heights[c]:
                    width_for_col += 1
                    r += 1
                while l >= 0 and heights[l] >= heights[c]:
                    width_for_col += 1
                    l -= 1
            areas.append(heights[c] * width_for_col)

        return max(areas)
