class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if(rowIndex == 1):
            nl2 = []
            nl2.append(1)
            nl2.append(1)
            return nl2
        if rowIndex == 2:
            nl3 = []
            nl3.append(1)
            nl3.append(2)
            nl3.append(1)
            return nl3
        nl1 = []
        nl = []
        nl.append(1)
        nl1.append(nl)
        if(rowIndex == 0):
            return nl
        del nl
        nl = []
        nl.append(1)
        nl.append(1)
        nl1.append(nl)
        if(rowIndex == 2):
            return nl
        del nl
        nl = []
        a = nl1[len(nl1) - 1]
        for i in range(0 , rowIndex - 1):
            nl.append(1)
            for i in range(0 , len(a) - 1):
                nl.append(a[i] + a[i + 1])
            nl.append(1)
            nl1.append(nl)
            del a
            a = []
            for i in nl:
                a.append(i)
            del nl
            nl = []
        return nl1[len(nl1) - 1]