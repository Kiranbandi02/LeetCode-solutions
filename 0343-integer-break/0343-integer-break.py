class Solution:
    def integerBreak(self, n: int) -> int:
        dp={1:1}
        def r(num):
            if(num in dp):
                return dp[num]
            res=0 if num==n else num
            for i in range(1,num):
                v=r(i)*r(num-i)
                res=max(res,v)
            dp[num]=res
            return dp[num]
        return r(n)