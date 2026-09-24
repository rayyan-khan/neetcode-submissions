class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = dict()
        for n in nums:
            numCount[n] = 1 + numCount.get(n, 0)
            
        sortedByValueNumCount = sorted(numCount.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sortedByValueNumCount[:k]]
        
        
            