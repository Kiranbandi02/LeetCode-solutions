class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in d:
            if(d[i]==2):
                l.append(i)
        return l