class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        if len(player1) == 1 and len(player2) == 1:
            if player1[0] > player2[0]:
                return 1
            elif player2[0] > player1[0]:
                return 2
            else:
                return 0
        sp1 = 0
        sp1 += player1[0]
        if(player1[0] == 10):
            sp1 += 2 * player1[1]
        else:
            sp1 += player1[1]
        sp2 = 0
        sp2 += player2[0]
        if player2[0] == 10:
            sp2 += 2 * player2[1]
        else:
            sp2 += player2[1]
        for i in range(2 , len(player1)):
            if(player1[i - 1] == 10 or player1[i - 2] == 10):
                sp1 += 2 * player1[i]
            else:
                sp1 += player1[i]
        for i in range(2 , len(player2)):
            if(player2[i - 1] == 10 or player2[i - 2] == 10):
                sp2 += 2 * player2[i]
            else:
                sp2 += player2[i]
        if sp1 > sp2:
            return 1
        elif sp2 > sp1:
            return 2
        else:
            return 0