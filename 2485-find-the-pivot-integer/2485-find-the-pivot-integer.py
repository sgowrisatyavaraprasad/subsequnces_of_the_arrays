class Solution:
    def pivotInteger(self, n: int) -> int:
        nl = []
        ps = 0
        for i in range(1 , n + 1):
            ps += i
            a = sum(range(i , n + 1))
            if a == ps:
                return i
        return -1