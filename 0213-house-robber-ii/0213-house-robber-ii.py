class Solution:
    def rob(self, nums: List[int]) -> int:
        def h(a):
            n=len(a)
            dp=[0]*n
            dp[0]=a[0]
            for i in range(1,n):
                t=a[i]
                if(i>1):
                    t+=dp[i-2]
                nt=dp[i-1]
                dp[i]=max(t,nt)
            return dp[n-1]
        if(len(nums)==1):
            return nums[0]
        a=h(nums[:len(nums)-1])
        b=h(nums[1:])
        return max(a,b)