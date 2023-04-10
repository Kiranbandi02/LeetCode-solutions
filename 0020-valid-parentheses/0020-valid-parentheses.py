class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if(i=="(" or i=="{" or i=="["):
                st.append(i)
            else:
                if(st==[]):
                    return 0
                if(st[-1]=="(" and i==")"):
                    st.pop(-1)
                elif(st[-1]=="[" and i=="]"):
                    st.pop(-1)
                elif(st[-1]=="{" and i=="}"):
                    st.pop(-1)
                else:
                    return 0
        if(st!=[]):
            return 0
        return 1