class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        m=float("inf")
        for i in range(len(nums)-1):
            m=min(m,nums[i+1]-nums[i])
        return m