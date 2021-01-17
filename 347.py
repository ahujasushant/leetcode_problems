class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        result = list(d.keys())[-k:]
        return result

