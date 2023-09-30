class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st=[]
        cur=nums[0]
        for i in nums[1:]:
            while st and i>=st[-1][0]:
                st.pop()
            if(st and i<st[-1][0] and i>st[-1][1]):
                return True
            st.append([i,cur])
            cur=min(cur,i)
        return False
        