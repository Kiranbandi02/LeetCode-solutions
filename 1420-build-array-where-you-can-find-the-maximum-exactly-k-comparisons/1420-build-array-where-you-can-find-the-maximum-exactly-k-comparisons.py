class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]
        MOD = 10 ** 9 + 7
        
        for num in range(1, m + 1):
            dp[1][num][1] = 1
            
        for i in range(1, n + 1):
            for max_num in range(1, m + 1):
                for cost in range(1, k + 1):                    
                    ans = (max_num * dp[i - 1][max_num][cost]) % MOD
                    
                    for num in range(1, max_num):
                        ans = (ans + dp[i - 1][num][cost - 1]) % MOD

                    dp[i][max_num][cost] += ans
                    dp[i][max_num][cost] %= MOD
    
        ans = 0
        for num in range(1, m + 1):
            ans = (ans + dp[n][num][k]) % MOD
        
        return ans