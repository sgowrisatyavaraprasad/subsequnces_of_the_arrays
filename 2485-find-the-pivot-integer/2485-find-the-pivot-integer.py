class Solution:
    def pivotInteger(self, n: int) -> int:
        nl = []
        for i in range(1 , n + 1):
            nl.append(i)

        for i in range(0 , len(nl)):
            a = sum(nl[0 : i + 1])
            b = sum(nl[i : len(nl)])
            if a == b:
                return nl[i]
        return -1