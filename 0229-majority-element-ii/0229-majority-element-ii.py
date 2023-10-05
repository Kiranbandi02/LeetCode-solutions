class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for i in nums:
            if( i in d):
                d[i]+=1
            else:
                d[i]=1
            if(d[i]>len(nums)//3):
                l.append(i)
       #l=[]
        #or i in d:
         #  if(d[i]>len(nums)//3):
          #     l.append(i)
        return list(set(l))
                
        