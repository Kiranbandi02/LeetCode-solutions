class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]*len(nums)
        r=[1]*len(nums)
        n=len(nums)
        for i in range(1,n):
            l[i]=l[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            r[i]=r[i+1]*nums[i+1]
        for i in range(n):
            nums[i]=r[i]*l[i]
        return nums