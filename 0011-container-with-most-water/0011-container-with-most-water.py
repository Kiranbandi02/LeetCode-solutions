class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,a=0,len(height)-1,0
        ans=0
        while l<=r:
            a=(r-l)*min(height[l],height[r])
            ans=max(ans,a)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return ans