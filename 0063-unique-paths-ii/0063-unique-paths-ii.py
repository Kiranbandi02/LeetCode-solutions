class Solution:
    def uniquePathsWithObstacles(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        dp=[]
        for i in range(n):
            dp.append([-1]*m)
        for i in range(n):
            for j in range(m):
                if(i==0 and j==0):
                    if(mat[i][j]==1):
                        dp[i][j]=0
                    else:
                        dp[i][j]=1
                elif(mat[i][j]==1):
                    dp[i][j]=0
                else:
                    u,d=0,0
                    if(i>0):
                        u=dp[i-1][j]
                    if(j>0):
                        d=dp[i][j-1]
                    dp[i][j]=u+d
        return dp[n-1][m-1]