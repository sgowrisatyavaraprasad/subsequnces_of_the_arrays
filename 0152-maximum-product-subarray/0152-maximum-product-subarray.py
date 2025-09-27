class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        suf = 1
        m = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(0 , len(nums)):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
            pre = pre * nums[i]
            suf = suf * nums[len(nums) - i - 1]
            m = max(m , max(pre , suf))
        return m