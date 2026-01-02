class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = len(nums) - 1
        nl = []
        c = 0
        while(a >= 0):
            c += 1
            cc = 0
            nl.append(nums[a])
            for i in range(1 , k + 1):
                if i in nl:
                    cc += 1
            if cc == k:
                return c
            a -= 1
        return 0