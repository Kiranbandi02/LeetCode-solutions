class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        k=list(permutations(nums,len(nums)))
        o=[]
        for i in k:
            o.append(list(i))
        return o