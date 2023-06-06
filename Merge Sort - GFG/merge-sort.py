#User function Template for python3

class Solution:
    def merge(self,arr):
        if(len(arr)>1):
            mid=len(arr)//2
            l=arr[:mid]
            r=arr[mid:]
            self.merge(l)
            self.merge(r)
            i,j,r1=0,0,0
            while i<len(l) and j<len(r):
                if(l[i]<=r[j]):
                    arr[r1]=l[i]
                    i+=1
                    r1+=1
                else:
                    arr[r1]=r[j]
                    j+=1
                    r1+=1
            while i<len(l):
                arr[r1]=l[i]
                i+=1
                r1+=1
            while j<len(r):
                arr[r1]=r[j]
                j+=1
                r1+=1
            return arr
        
        
        
    def mergeSort(self,arr, l, r):
        #code here
        return self.merge(arr)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends