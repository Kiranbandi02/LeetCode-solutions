class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q

        return min(1, A[query_row][query_glass])























"""
class Solution:
    def champagneTower(self, p: int, query_row: int, query_glass: int) -> float:
        dp=[]
        for i in range(1,101):
            dp.append([0]*i)
        i=0
        while p>0 and i<100:
            
            if(len(dp[i])<=p):
                dp[i]=[1]*(i+1)
                p=p-(i+1)
                i+=1
                print(dp[i-1],p)
            elif(p==0):
                break
                print(dp[i-1],p)
            elif(p<len(dp[i])):
                for j in range(i+1):
                    dp[i][j]=p
                    q=(p-1.0)/2.0
                    if(q>0):
                        dp[i][j]+=q
                        dp[i][j+1]+=q
                        
                
                        
                
                
                #dp[i]=[p/(i+1)]*(i+1)
                #i=i+1
                #p=0
                #print(dp[i-1],p)
                #break
        return dp[query_row][query_glass]
      """      