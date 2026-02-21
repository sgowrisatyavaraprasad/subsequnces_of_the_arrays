class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c = 0
        for i in range(left , right + 1):
            a = bin(i)
            b = a.count('1')
            fc = 0
            for j in range(1 , b + 1):
                if b % j == 0:
                    fc += 1
            if fc == 2:
                c += 1
        return c