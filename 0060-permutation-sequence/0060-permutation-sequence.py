class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from itertools import permutations
        l=[str(i) for i in range(1,n+1)]
        p=list(permutations(l,len(l)))
        o=[]
        for i in p:
            o.append(int("".join(i)))
        o.sort()
        return str(o[k-1])