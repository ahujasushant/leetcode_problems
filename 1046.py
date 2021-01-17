class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        so = sorted(stones)
        while (len(so) > 1):
            e1 = so.pop()
            e2 = so.pop()
            if e1 != e2:
                so.append(e1 - e2)
                so = sorted(so)

        if len(so) == 1:
            return so[0]
        return 0

