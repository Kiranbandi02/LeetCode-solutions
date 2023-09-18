class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l=[]
        for i,j in enumerate(mat):
            l.append([j.count(1),i])
        a=[]
        l.sort()
        for i in range(len(l)):
            a.append(l[i][1])
        return a[:k]