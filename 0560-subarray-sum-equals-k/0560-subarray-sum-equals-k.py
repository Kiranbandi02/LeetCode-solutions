class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        d={0:1}
        p=0
        for i in nums:
            p+=i
            if(p-k in d):
                c+=d[p-k]
                #d[p-k]+=1
                #d[p]+=1
            #else:
            if(p not in d):
                d[p]=1
            else:
                d[p]+=1
            #d[p]=1
        return c
                
                
        
                