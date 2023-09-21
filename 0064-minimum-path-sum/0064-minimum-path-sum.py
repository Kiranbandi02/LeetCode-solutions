class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def r(i,j):
            #print(i,j,s)
            if(i==0 and j==0):
                return grid[0][0]
            if(i<0 or j<0):
                return float("inf")
            if(dp[i][j]!=-1):
                return dp[i][j]
            dp[i][j]=min(grid[i][j]+r(i,j-1),grid[i][j]+r(i-1,j))
            return dp[i][j]
        m=len(grid)
        n=len(grid[0])
        dp=[]
        for i in range(m):
            dp.append([-1]*n)
        #print(dp)
        r(m-1,n-1)
        dp[0][0]=grid[0][0]
        return dp[m-1][n-1]
        