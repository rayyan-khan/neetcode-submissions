class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = max(1, sum(piles)//h)
        right = max(piles)
        res = right

        while left <= right:
            mid_speed = (left + right)//2

            totalTime = 0
            for p in piles:
                totalTime += -(-p // mid_speed)

            if totalTime <= h:
                res = mid_speed
                right = mid_speed - 1
            else:
                left = mid_speed + 1
        return res

