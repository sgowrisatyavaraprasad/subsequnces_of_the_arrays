class Solution:
    def totalMoney(self, n: int) -> int:
        nl = []
        if(n <= 7):
            s = 0
            for i in range(1 , n + 1):
                s += i
            return s
        else:
            s = 0
            for i in range(1 , 8):
                s += i
                nl.append(i)
            a = 8
            while(a <= n):
                s += nl[len(nl) - 7] + 1
                nl.append(nl[len(nl) - 7] + 1)
                a += 1
            
            return s
        return 0