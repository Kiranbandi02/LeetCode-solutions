class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=1
        l=0
        for r in range(len(nums)):
            n-= nums[r]==0
            if(n<0):
                n+= nums[l]==0
                l+=1
        return r-l
                