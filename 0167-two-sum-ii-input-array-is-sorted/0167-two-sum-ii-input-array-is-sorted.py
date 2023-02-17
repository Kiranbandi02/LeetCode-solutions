class Solution:
    def twoSum(self, nu: List[int], target: int) -> List[int]:
        i=0
        j=len(nu)-1
        while(i<j):
            if(nu[i]+nu[j]==target):
                return [i+1,j+1]
            elif(nu[i]+nu[j]>target):
                j-=1
            else:
                i+=1