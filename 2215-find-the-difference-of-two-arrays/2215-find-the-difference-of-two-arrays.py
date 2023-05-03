class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[]
        k=[]
        for i in nums1:
            if(i not in nums2):
                k.append(i)
        l.append(list(set(k)))
        k=[]
        for i in nums2:
            if(i not in nums1):
                k.append(i)
        l.append(list(set(k)))
        return l