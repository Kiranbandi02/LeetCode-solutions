class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        k=[]
        nums.sort()
        for i in range(len(nums)):
            a=-nums[i]
            l=i+1
            h=len(nums)-1
            while l<h:
                if(nums[l]+nums[h]==a):
                    l1=[nums[i],nums[l],nums[h]]
                    if(l1 not in k):
                        k.append(l1)
                    l+=1
                    h-=1
                elif(nums[l]+nums[h]<a):
                    l+=1
                else:
                    h-=1
        return k