class Solution:
    def pivotInteger(self, n: int) -> int:
        nl = []
        ps = 0
        for i in range(1 , n + 1):
            nl.append(i)

        for i in range(0 , len(nl)):
            ps += nl[i]
            b = sum(nl[i : len(nl)])
            if ps == b:
                return nl[i]
        return -1