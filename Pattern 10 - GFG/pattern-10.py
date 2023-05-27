#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1,N+1):
            s=i
            b=(N-s)
            print(b*""+s*"* "+b*" ")
        for i in range(N-1,0,-1):
            s=i
            b=(N-s)
            print(b*""+s*"* "+b*" ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends