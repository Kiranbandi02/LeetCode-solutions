class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        d={0:1}
        p=0
        c=0
        for i in nums:
            p+=i
            if(p-k in d):
                c+=d[p-k]
            if(p in d):
                d[p]+=1
            else:
                d[p]=1
        return c