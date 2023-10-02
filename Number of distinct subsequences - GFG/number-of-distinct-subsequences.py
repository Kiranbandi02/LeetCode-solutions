#User function Template for python3

class Solution:
	def distinctSubsequences(self, S):
		# code here
		mod=10**9+7
		la={}
		n=len(S)
		dp=[0]*(n+1)
		dp[0]=1
		for i in range(1,n+1):
		    dp[i]=(dp[i-1]*2)%mod
		    ch=S[i-1]
		    if(ch in la):
		        j=la[ch]
		        dp[i]-=dp[j]
		    la[ch]=i-1
	    return dp[-1]%mod
		    
		    
		    
		    
		    
		 
		
		
		
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends