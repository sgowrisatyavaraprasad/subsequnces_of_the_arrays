class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        f = {}
        f[0] = 1
        ps = 0
        c = 0
        for i in range(0 , len(nums)):
            ps += nums[i]
            a = ps - k
            if a in f:
                c += f[a]
            if a not in f:
                pass
            if ps in f:
                f[ps] += 1
            else:
                f[ps] = 1
        return c