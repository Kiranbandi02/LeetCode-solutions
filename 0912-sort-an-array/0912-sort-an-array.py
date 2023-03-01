class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
        
        
        """
        t=[0]*len(nums)
        def merge(l,m,h):
            s1=l
            s2=m+1
            n1=m-l+1
            n2=h-m
            for i in range(n1):
                t[s1+i]=nums[s1+i]
            for i in range(n2):
                t[s2+i]=nums[s2+i]
            i,j=0,0
            k=l
            while i<n1 and j<n2:
                if(t[s1+i]<=t[s2+j]):
                    nums[k]=t[s1+i]
                    i+=1
                else:
                    nums[k]=t[s2+j]
                    j+=1
                k+=1
            while i<n1:
                nums[k]=t[s1+i]
                i+=1
                k+=1
            while j<n2:
                nums[k]=t[s2+j]
                j+=1
                k+=1
        def merge_sort(l,h):
            if(l>=h):
                return
            m=(l+h)//2
            merge_sort(l,m)
            merge_sort(m+1,h)
            merge(l,m,h)
        merge_sort(0,len(nums)-1)
        return nums"""
        
    