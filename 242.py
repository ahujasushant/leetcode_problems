class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        for c in s:
            if c in anagram:
                anagram[c] += 1
            else:
                anagram[c] = 1
        for c in t:
            if c in anagram:
                if anagram[c] <= 0:
                    return False
                anagram[c] -= 1
            else:
                return False
        for value in anagram.values():
            if value != 0:
                return False
        return True