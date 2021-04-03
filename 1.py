class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain_nums = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in remain_nums:
                return [remain_nums[res], i]
            else:
                remain_nums[nums[i]] = i