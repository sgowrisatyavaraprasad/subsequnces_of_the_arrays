class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = {}
        cout  = 0
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        a = max(f.values())
        for key,values in f.items():
            if a == values:
                cout += 1
        return a * cout