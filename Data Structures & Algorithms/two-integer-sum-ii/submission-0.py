class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        val_idx = dict()
        for k in range(len(numbers)):
            val_idx[numbers[k]] = k+1
        
        for i in range(len(numbers)):
            val = numbers[i]
            if target-val in val_idx:
                return [i+1, val_idx[target-val]]

        