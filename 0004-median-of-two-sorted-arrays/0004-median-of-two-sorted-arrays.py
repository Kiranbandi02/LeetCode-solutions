import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        d=sorted(nums1+nums2)
        k=statistics.median(d)
        return k