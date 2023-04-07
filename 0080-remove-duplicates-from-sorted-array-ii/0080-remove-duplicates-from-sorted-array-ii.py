class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            if(nums.count(nums[i])>2):
                nums[i]=float('inf')
                c+=1
        nums.sort()
        return len(nums)-c
        