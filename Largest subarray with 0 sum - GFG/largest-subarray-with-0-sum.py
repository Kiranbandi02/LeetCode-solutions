#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        d={}
        s=0
        ma=0
        for i in range(n):
            s=s+arr[i]
            if(s==0):
                ma=i+1
            else:
                if(s in d):
                    ma=max(ma,i-d[s])
                else:
                    d[s]=i
        return ma
    

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends