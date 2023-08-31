class Solution:
    def findScore(self, nums: List[int]) -> int:
        s=[0]*(len(nums)+1)
        sc=0
        for a,i in sorted([a,i] for i,a in enumerate(nums)):
            if(s[i]):
                continue
            sc+=a
            s[i]=s[i-1]=s[i+1]=1
        return sc