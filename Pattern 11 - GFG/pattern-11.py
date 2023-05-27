#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        k=""
        for i in range(1,N+1):
            if(k==""):
                k="1"
            elif(k[0]=="1"):
                k="0 "+k
            else:
                k="1 "+k
            print(k)


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