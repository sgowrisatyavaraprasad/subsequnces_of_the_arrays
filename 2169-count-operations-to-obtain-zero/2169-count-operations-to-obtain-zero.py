class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        c = 0
        while num1 != 0 and num2 != 0:
            c += 1
            if num1 < num2:
                num2 = num2 - num1
            elif num1 > num2:
                num1 = num1 - num2
            else:
                num1 = num1 - num2
        return c