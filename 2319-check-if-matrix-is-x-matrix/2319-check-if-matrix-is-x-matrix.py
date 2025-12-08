class Solution:
    def checkXMatrix(self, mat: List[List[int]]) -> bool:
        i1 = 0
        j1 = 0
        i2 = 0
        j2 = len(mat) - 1
        dc = 0
        nl = []
        while(i1 < len(mat) and j1 < len(mat) and i2 < len(mat) and j2 >= 0):
            if mat[i1][j1] != 0 and mat[i2][j2] != 0:
                dc += 1
                nl.append([i1 , j1])
                nl.append([i2 , j2])
            else:
                return False
            i1 += 1
            j1 += 1
            i2 += 1
            j2 -= 1
        a = 0
        allc = 0
        for i in range(0 , len(mat)):
            for j in range(0 , len(mat[i])):
                if [i , j] not in nl:
                    if mat[i][j] == 0:
                        allc += 1
                    else:
                        return False
        i = 1
        b = int(len(mat) / 2)
        pc = 0
        print(b)
        if len(mat) % 2 == 0:
            for i in range(0 , b - 1):
                c = i + 1
                d = len(mat) - i - 1
                while(c < d):
                    if mat[j][c] == 0:
                        pc += 1
                    c += 1
        else:
            for i in range(0 , b):
                c = i + 1
                d = len(mat) - i - 1
                while(c < d):
                    if mat[j][c] == 0:
                        pc += 1
                    c += 1
        if allc == 4 * pc and dc == len(mat):
            return True
        return False