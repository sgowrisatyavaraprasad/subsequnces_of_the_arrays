class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        nl = []
        nl1 = []
        l = 0
        r = k - 1
        if k == len(nums):
            return max(nums)
        while r < len(nums):
            for i in range(l , r+1):
                nl.append(nums[i])
            nl1.append(nl)
            l += 1
            r += 1
        a = nl1[0]
        f = {}
        for i in a:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        b = []
        for key , values in f.items():
            if values == 1:
                b.append(key)
        print(nl1)
        print(f)
        if len(b) == 0:
            return -1
        else:
            return max(b)