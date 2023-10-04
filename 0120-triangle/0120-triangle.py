class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        s=0
        dp=[]
        for i in range(len(t)):
            dp.append([0]*len(t[i]))
            for j in range(len(t[i])):
                if(i==0):
                    dp[i][j]=t[i][j]
                else:
                    if(j>0 and j<len(t[i-1])):
                        #print(i,j)
                        dp[i][j]=t[i][j]+min(dp[i-1][j],dp[i-1][j-1])
                    else:
                        if(j>=len(t[i-1])-1):
                            dp[i][j]=t[i][j]+dp[i-1][j-1]
                        else:
                            dp[i][j]=t[i][j]+dp[i-1][j]
        print(dp)
        return min(dp[-1])
                