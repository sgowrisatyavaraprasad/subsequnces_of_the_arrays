class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        nl = []
        s = 0
        c1 = 0
        c2 = 0
        for i in bank:
            if '1' in i:
                nl.append(i)
        for i in range(0 , len(nl) - 1):
            for j in nl[i]:
                if j == '1':
                    c1 += 1
            for k in nl[i + 1]:
                if k == '1':
                    c2 += 1
            s += (c1 * c2)
            
            c1 = 0
            c2 = 0
        return s