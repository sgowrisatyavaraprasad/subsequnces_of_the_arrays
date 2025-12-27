class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        nl = []
        nl.append(0)
        for i in range(0 , len(nums)):
            nl.append(nums[i])
        s = 0
        for i in range(1 , len(nl)):
            if n % i == 0:
                a = nl[i] * nl[i]
                s += a
        return s