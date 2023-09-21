class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=sorted(nums1+nums2)
        if(len(l)%2==0):
            m=len(l)//2
            return (l[m]+l[m-1])/2
        else:
            return l[len(l)//2]
            
        