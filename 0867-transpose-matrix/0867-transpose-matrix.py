class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nl = []
        for i in range(0 , len(matrix[0])):
            a = 0
            nl1 = []
            while(a < len(matrix)):
                nl1.append(matrix[a][i])
                a += 1
            nl.append(nl1)
        return nl