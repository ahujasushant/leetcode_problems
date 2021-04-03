class Solution(object):
    def maxSubArray(self, nums):
        rs = nums[0]
        ms = rs

        for num in nums[1:]:
            rs = max(rs + num, num)
            ms = max(ms, rs)

        return ms