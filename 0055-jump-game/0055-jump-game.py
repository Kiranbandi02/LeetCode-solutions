class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r=0
        for i in range(len(nums)):
            if(i>r):
                return 0
            r=max(r,i+nums[i])
        return 1
        
        
        
        
        """
        n=len(nums)
        def r(i):
            if(i>n-1):
                return 0
            if(i==n-1):
                return 1
            o=0
            for j in range(1,nums[i]+1):
                if(i+j!=i):
                    o+=r(i+j)
                if(o>0):
                    return o
            return o
        k=r(0)
        return k>0
        """
            