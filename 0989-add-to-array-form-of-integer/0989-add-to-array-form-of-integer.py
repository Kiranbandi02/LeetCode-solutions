class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a=int("".join([str(i) for i in num]))+k
        k=list(str(a))
        return [int(i) for i in k]