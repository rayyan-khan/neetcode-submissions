class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            middle = (l+r)//2
            val = nums[middle]
            if val == target:
                return middle
            elif val < target:
                l = middle + 1
            else:
                r = middle - 1
        return -1