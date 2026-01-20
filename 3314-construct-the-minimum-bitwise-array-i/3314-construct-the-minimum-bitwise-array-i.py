class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        nl =[]
        for i in range(0 , len(nums)):
            if nums[i] % 2 == 0:
                nl.append(-1)
            for j in range(1 , nums[i] + 1):
                a = (j) | (j + 1)
                if a == nums[i]:
                    nl.append(j)
                    break
        return nl