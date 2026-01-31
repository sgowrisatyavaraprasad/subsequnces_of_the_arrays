class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a = num / 3
        b = int(a)
        nl = []
        if(b * 3 == num):
            nl.append(b - 1)
            nl.append(b)
            nl.append(b + 1)
            return nl
        else:
            return nl
        return 0