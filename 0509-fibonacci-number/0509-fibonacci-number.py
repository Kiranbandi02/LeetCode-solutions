class Solution:
    def fib(self, n: int) -> int:
        if(n<3):
            f=[0,1,1]
            return f[n]
        else:
            f=[0]*(n+1)
            f[0]=0
            f[1]=1
            f[2]=1
            for i in range(3,n+1):
                f[i]=f[i-1]+f[i-2]
            return f[n]
        