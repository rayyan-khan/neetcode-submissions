class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix and suffix array approach
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        leftMax[0] = height[0]
        rightMax[len(height)-1] = height[len(height)-1]

        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
            rightMax[len(height)-1-i] = max(rightMax[len(height)-i], height[len(height)-1-i])
        
        running_total = 0

        for k in range(1, len(height)-1):
            running_total += min(leftMax[k], rightMax[k]) - height[k]
        
        return running_total


            