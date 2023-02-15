class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        l=[]
        c=0
        if(k==0):
            for i in nums:
                if(nums.count(i)>1 and i not in l):
                    c+=1
                    l.append(i)
            return c
        for i in nums:
            if(i+k in nums and min(i,i+k) not in l):
                c+=1
                l.append(min(i,i+k))
        return c