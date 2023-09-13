#User function Template for python3

class Solution:
    def findLargest(self, n, s):
        # code here
        o=""
        if(s==0 and N!=1):
            return -1
        while n>0 :
            for i in range(9,-1,-1):
                if(i==9 and s>i):
                    s=s-i
                    o+=str(i)
                    break
                elif(i==s):
                    s=s-i
                    o+=str(i)
                    break
            n-=1
        if(s!=0):
            return -1
        return int(o)
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends