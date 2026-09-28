class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        val_idx = {nums[i]:i for i in range(len(nums))}
        solutions = set()
        for j in range(len(nums)):
            for k in range(len(nums)):
                if j != k:
                    complement = 0 - (nums[j] + nums[k])
                    if complement in val_idx and val_idx[complement] not in (j,k):
                        potential_solution = tuple(sorted([complement, nums[j], nums[k]]))
                        if potential_solution not in solutions:
                            solutions.add(potential_solution)
        return list(solutions)

        