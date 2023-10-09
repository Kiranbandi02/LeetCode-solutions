class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        if(target not in d):
            return [-1,-1]
        return [d[target][0],d[target][-1]]