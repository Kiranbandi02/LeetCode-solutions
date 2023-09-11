class Solution:
    def groupThePeople(self, g: List[int]) -> List[List[int]]:
        d={}
        for i in range(len(g)):
            if(g[i] not in d):
                d[g[i]]=[i]
            else:
                k=d[g[i]]
                k.append(i)
                d[g[i]]=k
        l=[]
        for i in d:
            k=d[i]
            j=0
            while i+j<=len(k):
                l.append(k[j:i+j])
                j+=i
        return l