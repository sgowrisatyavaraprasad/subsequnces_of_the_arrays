class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums) == 1:
            return math.ceil(nums[0] / threshold)
        low = 1
        high = max(nums)
        nl = []
        while(low <= high):
            mid = int((low + high) / 2)
            nl1 = []
            for i in nums:
                nl1.append(math.ceil(i / mid))
            a = sum(nl1)
            if a <= threshold:
                nl.append(mid)
                high = mid - 1
            else:
                low = mid + 1
        print(nl)
        if len(nl) == 0:
            return max(nums)
        else:
            return min(nl)