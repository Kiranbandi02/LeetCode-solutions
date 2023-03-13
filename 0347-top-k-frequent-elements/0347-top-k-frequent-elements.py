class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if(i not in d):
                d[i]=1
            else:
                d[i]+=1
        l=[]
        for i in d:
            l.append([i,d[i]])
        l.sort(key=lambda x:x[1],reverse=True)
        d=[]
        for i in range(k):
            d.append(l[i][0])
        return d