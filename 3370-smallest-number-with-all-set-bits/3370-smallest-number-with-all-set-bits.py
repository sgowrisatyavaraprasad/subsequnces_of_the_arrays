class Solution:
    def smallestNumber(self, n: int) -> int:
        nl = []
        for i in range(1 , 2 * n):
            a = bin(i)
            b = str(a)
            nl1 = []
            for j in range(2 , len(b)):
                nl1.append(b[j])
            c = list(set(nl1))
            print(c)
            if c[0] == "1" and len(c) == 1:
                nl.append(int(a , 2))
        print(nl)
        return max(nl)