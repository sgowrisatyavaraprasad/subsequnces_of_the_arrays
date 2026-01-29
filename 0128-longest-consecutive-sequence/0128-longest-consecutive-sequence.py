class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        a = sorted(list(set(nums)))
        c = 1
        nl = []
        b = a[0]
        m = 0
        for i in range(1 , len(a)):
            if b + 1 == a[i]:
                c += 1
                b = a[i]
            else:
                m = max(m ,c)
                c = 1
                b = a[i]
        m = max(m , c)
        return m