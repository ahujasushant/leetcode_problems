class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        extra = []
        remove_p = []
        for i,c in enumerate(list(s)):
            if c == "(":
                extra.append(i)
            elif c == ")":
                if len(extra) == 0:
                    remove_p.append(i)
                else:
                    extra.pop()
        while len(extra) > 0:
            remove_p.append(extra.pop(0))

        for i in remove_p[::-1]:
            s = s[:i]+s[i+1:]
        return s
