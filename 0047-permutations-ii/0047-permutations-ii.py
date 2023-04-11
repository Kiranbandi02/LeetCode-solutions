class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        l=set(permutations(nums))
        return list(l)