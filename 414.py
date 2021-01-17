class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if nums is None: return None
        if len(nums) < 3: return max(nums)
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
        arr = list(d.keys())
        if len(arr) < 3: return max(arr)
        return list(d.keys())[-3]
