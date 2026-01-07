class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = 0
        for i in range(0 , len(nums)):
            a += nums[i]
            b = sum(nums[i : len(nums)])
            if a == b:
                return i
        return -1