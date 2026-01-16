class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        nl = []
        l = 0
        r = 0
        c = 0
        s = 0
        while(r < len(nums)):
            s += nums[r]
            c += 1
            if c >= k:
                a = s / k
                nl.append(a)
                s -= nums[l]
                l += 1
                r += 1
                continue
            if r == len(nums) - 1:
                l += 1
            r += 1
        return max(nl)