class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = bin(n)
        for i in range(2 , len(a) - 1):
            if a[i] == a[i + 1]:
                return False
        return True
