class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0 , len(nums)):
            a = sum(nums[0 : i + 1])
            b = sum(nums[i : len(nums)])
            if a == b:
                return i
        return -1