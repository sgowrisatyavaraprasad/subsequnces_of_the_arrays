class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)
        nl = []
        for i in range(len(a) - 1 , 1 , -1):
            nl.append(a[i])
        c = ''.join(nl)
        a = len(c)
        for i in range(a + 1 , 33):
            c += '0'
        d = int(c , 2)
        print(d)
        return d