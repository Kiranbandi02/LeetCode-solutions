class Solution:
    def minFallingPathSum(self, a: List[List[int]]) -> int:
        n,m=len(a),len(a[0])
        dp=[]
        for i in range(n):
            dp.append([0]*m)
        for i in range(n):
            for j in range(m):
                if(i==0):
                    dp[i][j]=a[i][j]
                else:
                    u=l=r=float("inf")
                    if(i>0 and j>0):
                        u=a[i][j]+dp[i-1][j-1]
                    if(i>0):
                        l=a[i][j]+dp[i-1][j]
                    if(i>0 and j<m-1):
                        r=a[i][j]+dp[i-1][j+1]
                    dp[i][j]=min(u,l,r)
        print(dp)
        return min(dp[n-1])
        """
        def r(i,j):
            if(i>n-1 or j>m-1 or i<0 or j<0):
                return float("inf")
            if(dp[i][j]!=-1):
                return dp[i][j]
            if(i==n-1):
                #print(a[i][j])
                #r()
                return a[i][j]
            u=a[i][j]+ r(i+1,j-1)
            l=a[i][j]+ r(i+1,j)
            r1=a[i][j]+ r(i+1,j+1)
            dp[i][j]=min(u,l,r1)
            return dp[i][j]
        n=len(a)
        m=len(a[0])
        dp=[]
        for i in range(n):
            dp.append([-1]*m)
        #j=a[0].index(min(a[0]))
        l=[]
        #r(0,0)
        #print(dp)
        for i in range(m):
            k=r(0,i)
            l.append(k)
        return(min(l))"""
            