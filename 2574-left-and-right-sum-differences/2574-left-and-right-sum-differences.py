class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[]
        r=[]
        n=len(nums)
        for i in range(n):
            l.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return l