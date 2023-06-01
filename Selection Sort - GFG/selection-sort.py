#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        j=arr.index(min(arr))
        return j
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)-1):
            k=self.select(arr[i:],i)
            arr[i],arr[k+i]=arr[i+k],arr[i]
        return arr
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends