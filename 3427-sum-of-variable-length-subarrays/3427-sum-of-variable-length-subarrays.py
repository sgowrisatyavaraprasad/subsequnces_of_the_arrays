class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ps = 0
        ps = nums[0]
        for i in range(1 ,  len(nums)):
            start = max(0 , i - nums[i])
            ps += sum(nums[start : i + 1])
        return ps