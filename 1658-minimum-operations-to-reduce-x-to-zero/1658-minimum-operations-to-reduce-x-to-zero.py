class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)
        
        if target == 0:
            return n
        
        max_len = cur_sum = left = 0
        
        for right, val in enumerate(nums):
            cur_sum += val
            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return n - max_len if max_len else -1 








    """class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l=[]
        i=0
        for j in range(len(nums)):
            
        
        
        
        
    
        def r(a,x,c):
            if(len(a)==0):
                return float("inf")
            if(x==0):
                return c
            if(len(a)>0 and x<0 or min(a)>x):
                return float("inf")
            n=len(a)-1
            return min(r(a[1:],x-a[0],c+1),r(a[:n],x-a[-1],c+1),r(a[1:],x,c+1),r(a[:n],x,c+1))
        if(min(nums)>x):
            return -1
        k=r(nums,x,0)
        if(k==float("inf")):
            return -1
        return(k)"""