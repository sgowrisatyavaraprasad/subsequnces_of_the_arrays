class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        a = sorted(arr)
        b = 0
        nl1 = []
        print(a)
        for i in range(0 , len(a) - 1):
            nl1.append(abs(a[i + 1] - a[i]))
        print(nl1)
        b = min(nl1)
        print(b)
        nl = []
        for i in range(0 , len(a) - 1):
            c = abs(a[i] - a[i + 1])
            if c == b:
                nl.append([a[i] , a[i + 1]])
        return nl