class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=sorted(nums)
        k=[]
        for i in nums:
            if(i not in k):
                k.append(i)
        if(len(k)<3):
            return k[-1]
        return k[-3]
            