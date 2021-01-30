class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        fa = False
        sa = False
        if len(arr) < 3: return False
        ile = arr.index(max(arr))
        i = ile
        while i < len(arr)-1:
            sa = True
            if arr[i+1] >= arr[i]:
                return False
            i += 1
        i = ile
        while i > 0:
            fa = True
            if arr[i-1] >= arr[i]:
                return False
            i -= 1
        return (fa and sa)
