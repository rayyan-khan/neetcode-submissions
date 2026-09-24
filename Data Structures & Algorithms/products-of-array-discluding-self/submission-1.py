class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            total_product = math.prod(nums)
            return [int(total_product/k) for k in nums]
        else:
            zero_count = nums.count(0)
            if zero_count > 1:
                return [0] * len(nums)

            total_product_sans_0 = math.prod([k for k in nums if k != 0])
            return [0 if k != 0 else total_product_sans_0 for k in nums]
        