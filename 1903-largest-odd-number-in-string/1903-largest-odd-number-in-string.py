class Solution:
    def largestOddNumber(self, num: str) -> str:
        import sys
        sys.set_int_max_str_digits(100000)
        a = int(num)
        if a % 2 != 0:
            return str(a)
        while a != 0:
            b = a % 10
            if(a % 2 != 0):
                return str(a)
                break
            a = a // 10
        return ""
            