class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ps = 0
        c = 0
        for i in range(0 , len(nums)):
            ps += nums[i]
            if ps == 0:
                c += 1
        return c
        