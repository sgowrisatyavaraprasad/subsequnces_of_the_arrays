class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nl = []
        for i in range(1 , 2000):
            nl.append(i)
        for i in arr:
            nl.remove(i)
        if(len(nl) < k):
            return 0
        else:
            return nl[k - 1]