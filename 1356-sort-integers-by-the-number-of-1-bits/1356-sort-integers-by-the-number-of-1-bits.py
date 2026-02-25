class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        f = {}
        for i , val in enumerate(arr):
            a = bin(arr[i])
            # print(a)
            b = a.count('1')
            if b not in f:
                f[b] = []
            f[b].append(arr[i])
            # print(f)
        print(f)
        a = sorted(f.keys())
        print(a)
        nl = []
        for i in range(0 , len(a)):
            b = sorted(f[a[i]])
            nl.extend(b)
        return nl