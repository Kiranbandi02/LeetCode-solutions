class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            t=nums[i]
            if(i>=2):
                t+=dp[i-2]
            nt=dp[i-1]
            dp[i]=max(t,nt)
        return dp[len(nums)-1]