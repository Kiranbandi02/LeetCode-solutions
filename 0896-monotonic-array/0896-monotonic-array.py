class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a=1
        b=1
        for i in range(len(nums)-1):
            if(nums[i+1]>nums[i]):
                a=0
                break
        for i in range(len(nums)-1):
            if(nums[i+1]<nums[i]):
                b=0
                break
        return a or b