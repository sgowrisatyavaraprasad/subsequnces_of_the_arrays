class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            f1 = {}
            for j in i:
                if j in f1:
                    f1[j] += 1
                else:
                    f1[j] = 1
            print(f1)
            for key , values in f1.items():
                if key != '.':
                    if values >= 2:
                        return False
        print()
        print()
        print()
        a = 0
        while(a < len(board[0])):
            f2 = {}
            for i in range(0 , len(board)):
                if board[i][a] in f2:
                    f2[board[i][a]] += 1
                else:
                    f2[board[i][a]] = 1
            print(f2)
            for key , values in f2.items():
                if values >= 2:
                    if key != '.':
                        return False
            a += 1
        f3 = {}
        for i in range(0 , 3):
            for j in range(0 , 3):
                if board[i][j] in f3:
                    f3[board[i][j]] += 1
                else:
                    f3[board[i][j]] = 1
        for key , values in f3.items():
            if key != '.':
                if values >= 2:
                    return False
        f4 = {}
        for i in range(0 , 3):
            for j in range(3 , 6):
                if board[i][j] in f4:
                    f4[board[i][j]] += 1
                else:
                    f4[board[i][j]] = 1
        for key , values in f4.items():
            if key != '.':
                if values >= 2:
                    return False
        f5 = {}
        for i in range(0 , 3):
            for j in range(6 , 9):
                if board[i][j] in f5:
                    f5[board[i][j]] += 1
                else:
                    f5[board[i][j]] = 1
        for key , values in f5.items():
            if key != '.':
                if values >= 2:
                    return False
        f6 = {}
        for i in range(3 , 6):
            for j in range(0 , 3):
                if board[i][j] in f6:
                    f6[board[i][j]] += 1
                else:
                    f6[board[i][j]] = 1
        for key , values in f6.items():
            if key != '.':
                if values >= 2:
                    return False
        f7 = {}
        for i in range(3 , 6):
            for j in range(3 , 6):
                if board[i][j] in f7:
                    f7[board[i][j]] += 1
                else:
                    f7[board[i][j]] = 1
        for key , values in f7.items():
            if key != '.':
                if values >= 2:
                    return False
        f8 = {}
        for i in range(3 , 6):
            for j in range(6 , 9):
                if board[i][j] in f8:
                    f8[board[i][j]] += 1
                else:
                    f8[board[i][j]] = 1
        for key , values in f8.items():
            if key != '.':
                if values >= 2:
                    return False
        f9 = {}
        for i in range(6 , 9):
            for j in range(0 , 3):
                if board[i][j] in f9:
                    f9[board[i][j]] += 1
                else:
                    f9[board[i][j]] = 1

        for key , values in f9.items():
            if key != '.':
                if values >= 2:
                    return False
        f10 = {}
        for i in range(6 , 9):
            for j in range(3 , 6):
                if board[i][j] in f10:
                    f10[board[i][j]] += 1
                else:
                    f10[board[i][j]] = 1
        for key , values in f10.items():
            if key != '.':
                if values >= 2:
                    return False
        f11 = {}
        for i in range(6 , 9):
            for j in range(6 , 9):
                if board[i][j] in f11:
                    f11[board[i][j]] += 1
                else:
                    f11[board[i][j]] = 1
        for key , values in f11.items():
            if key != '.':
                if values >= 2:
                    return False
        return True