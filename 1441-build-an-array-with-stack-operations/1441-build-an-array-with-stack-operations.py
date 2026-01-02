class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        a = max(target)
        nl = []
        for i in range(1 , a + 1):
            if i in target:
                nl.append("Push")
            else:
                nl.append("Push")
                nl.append("Pop")
        return nl