class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d=[]
        for a in points:
            di=sqrt((a[0])**2+a[1]**2)
            d.append([a,di])
        d=sorted(d,key=lambda x:x[1])
        l=[]
        for i in range(k):
            l.append(d[i][0])
        return l
        