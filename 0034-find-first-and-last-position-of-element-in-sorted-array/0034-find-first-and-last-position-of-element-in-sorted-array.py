class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st,ed=-1,-1
        n=len(nums)
        for i in range(n):
            if(nums[i]==target):
                st=i
                break
        for i in range(n-1,-1,-1):
            if(nums[i]==target):
                ed=i
                break
        return [st,ed]