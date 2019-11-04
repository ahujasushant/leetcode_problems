class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            list_of_nums = []
            while x:
                list_of_nums.append(x % 10)
                x = x // 10
            return list_of_nums == list_of_nums[::-1]
