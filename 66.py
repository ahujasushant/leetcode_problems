class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for n in digits:
            num += str(n)
        a = []
        for d in (str(int(num) + 1)):
            a.append(d)
        return a