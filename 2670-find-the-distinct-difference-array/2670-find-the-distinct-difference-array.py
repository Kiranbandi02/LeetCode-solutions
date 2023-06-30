class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        a=[]
        n=len(nums)
        for i in range(n):
            l=len(set(nums[:i+1]))
            r=len(set(nums[i+1:]))
            a.append(l-r)
        return a