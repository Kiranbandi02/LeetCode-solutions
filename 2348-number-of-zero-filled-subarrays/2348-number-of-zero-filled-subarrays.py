class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c=0
        a=0
        for i in nums:
            if i==0:
                a+=1
            else:
                a=0
            c+=a
        return c