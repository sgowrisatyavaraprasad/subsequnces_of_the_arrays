class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) % 2 != 0:
            i1 = 0
            j1 = 0
            i2 = 0
            j2 = len(mat) - 1
            s = 0
            while(i1 < len(mat) and j1 < len(mat) and i2 < len(mat) and j2 >= 0):
                if i1 == i2 and j1 == j2:
                    s += mat[i1][j1]
                else:
                    s += mat[i1][j1]
                    s += mat[i2][j2]
                i1 += 1
                j1 += 1
                i2 += 1
                j2 -= 1
            return s
        else:
            i1 = 0
            j1 = 0
            i2 = 0
            j2 = len(mat) - 1
            s = 0
            while(i1 < len(mat) and j1 < len(mat) and i2 < len(mat) and j2 >= 0):
                s += mat[i1][j1]
                s += mat[i2][j2]
                print(mat[i1][j1])
                print(mat[i2][j2])
                i1 += 1
                j1 += 1
                i2 += 1
                j2 -= 1
            return s