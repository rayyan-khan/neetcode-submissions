class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        count = 0
        for num in num_set:
            if num - 1 not in num_set:
                count = 0
                while num in num_set:
                    num = num+1
                    count = count+1
                    if count > max_count:
                        max_count = count
        return max_count
