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
            
            print(f"trapping: {trapping}")
            if trapping:
                print(f"adding {height[l] - height[r]} to running total")
                running_total += height[l] - height[r]
                r = r+1
            else:
                l = r
                r = r+1

        return running_total


            