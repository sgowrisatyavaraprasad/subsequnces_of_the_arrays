class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rc = 0
        cc = 0
        nl = []
        for i in range(1 , len(matrix) + 1):
            nl.append(i)
        for i in matrix:
            a = sorted(i)
            if a == nl:
                rc += 1
        for i in range(0 , len(matrix)):
            nl1 = []
            j = 0
            while(j < len(matrix)):
                nl1.append(matrix[j][i])
                j += 1
            b = sorted(nl1)
            if nl == b:
                cc += 1
        if rc != len(matrix) or cc != len(matrix):
            return False
        if rc == cc and rc == len(matrix) and cc == len(matrix):
            return True