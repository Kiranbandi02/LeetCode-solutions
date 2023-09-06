class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for i in nums:
            i.sort()
        s=0
        for i in range(len(nums[0])):
            l=[]
            for j in range(len(nums)):
                l.append(nums[j][i])
            s=s+max(l)
        return s