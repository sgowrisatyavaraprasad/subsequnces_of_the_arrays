class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a = sorted(intervals)
        nl = []
        nl1 = []
        for i in range(0 , len(a)):
            s = a[i][0]
            e = a[i][1]
            if len(nl1) != 0:
                b = nl1[len(nl1) - 1]
                print(b)
                if s >= b[0] and e <= b[1]:
                    continue
                elif b[1] >= s:
                    b[1] = e
                elif b[0] >= e and b[1] >= s:
                    nl1.append([b[0] , b[1]])
                else:
                    nl1.append([s , e])
            else:
                nl1.append(a[i])
        return nl1