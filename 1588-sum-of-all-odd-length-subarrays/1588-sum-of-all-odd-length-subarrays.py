class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        nl = []
        for i in range(0 , len(nums)):
            for j in range(i , len(nums)):
                a = nums[i : j + 1]
                if len(a) % 2 != 0:
                    nl.append(sum(a))
        return sum(nl)