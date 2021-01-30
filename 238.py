class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_right = [1] * len(nums)
        prod_left = [1] * len(nums)
        product_nums = []
        for i in range(len(nums) - 1):
            prod_left[i + 1] *= prod_left[i] * nums[i]
        for i in range(len(nums) - 1, 0, -1):
            prod_right[i - 1] *= prod_right[i] * nums[i]
        for i in range(len(nums)):
            product_nums.append(prod_left[i] * prod_right[i])

        return product_nums