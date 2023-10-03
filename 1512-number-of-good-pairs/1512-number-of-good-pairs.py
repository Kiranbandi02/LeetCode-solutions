class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        s=[]
        for i in nums:
            if(i in s):
                c+=s.count(i)
                s.append(i)
            else:
                s.append(i)
        return c