class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = dict()
        for n in nums:
            if n in numCount:
                numCount[n] += 1
            else:
                numCount[n] = 1

        sortedByValueNumCount = sorted(numCount.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sortedByValueNumCount[:k]]
        
        
            