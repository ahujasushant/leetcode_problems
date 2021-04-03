def anangram(s, t):
    dict: {}

    for i in s:
        if s[i] in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in t:
        if t[i] in dict:
            dict[i] -= 1
        else:
            return False
    for v in dict.values():
        if v != 0:
            return False
    return True
