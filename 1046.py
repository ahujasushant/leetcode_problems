class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones) > 1):
            e1 = max(stones)
            stones.remove(e1)
            e2 = max(stones)
            stones.remove(e2)
            if e1 != e2:
                stones.append(e1 - e2)

        if len(stones) == 1:
            return stones[0]
        return 0

