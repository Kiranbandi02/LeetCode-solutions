class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        c=0
        nums.sort()
        k=target
        n=len(nums)
        r=n-1
        res=0
        for i,left in enumerate(nums):
            while left+nums[r]>k and i<=r:
                r-=1
            if(i<=r):
                res+=(2**(r-i))
        return res%(10**9+7)
        
        