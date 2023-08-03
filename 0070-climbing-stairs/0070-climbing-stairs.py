class Solution:
    def climbStairs(self, n: int) -> int:
        d=[0]*(n+1)
        for i in range(n+1):
            if(i==0):
                d[i]=0
            if(i==1):
                d[i]=1
            if(i==2):
                d[i]=2
            if(i>2):
                d[i]=d[i-1]+d[i-2]
        return d[n]