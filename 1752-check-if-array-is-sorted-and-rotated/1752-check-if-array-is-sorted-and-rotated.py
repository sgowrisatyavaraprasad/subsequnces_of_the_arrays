class Solution:
    def check(self, nums: List[int]) -> bool:
        a = sorted(nums)
        b = 0
        nl = []
        for i in range(0 , len(nums) - 1):
            if nums[i] > nums[i + 1]:
                b = i + 1
                break
        if b == 0:
            return True
        for i in range(b , len(nums)):
            nl.append(nums[i])
        for i in range(0 , b):
            nl.append(nums[i])
        print(nl)
        print(a)
        if nl == a:
            return True
        else:
            return False