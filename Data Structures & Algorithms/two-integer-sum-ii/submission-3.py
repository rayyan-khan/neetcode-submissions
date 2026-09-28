class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            complement = target-numbers[i]
            check = self.binsearch(numbers, complement, i+1)
            if check > 0:
                return [i+1, check+1]
            
        
    def binsearch(self, nums: List[int], target: int, start: int) -> int:
        left, right = start, len(nums) - 1

        while left <= right:
            mid = left + (right-left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

        