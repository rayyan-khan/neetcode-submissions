# inefficient but correct. Too inefficient to pass all the test cases.
class Solution:
    def trap(self, height: List[int]) -> int:
        running_total = 0
        trapping = False
        l = 0
        r = 1

        while r < len(height)-1:
            if height[l] > height[r] and max(height[r:]) > height[r]:
                trapping = True
            else:
                trapping = False
            
            if trapping:
                max_bound = min(height[l], max(height[r:]))
                running_total += max_bound - height[r]
                r = r+1
            else:
                l = r
                r = r+1

        return running_total


            
