class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k=[]
        for i in nums:
            if(i%2==0):
                k.insert(0,i)
            else:
                k.append(i)
        return(k)
        