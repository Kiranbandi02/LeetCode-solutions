class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        l=[]
        le=0
        r=0
        for i in s:
            if(i=="("):
                le+=1
            if(i==")"):
                r+=1
            st.append(i)
            if(le==r):
                l.append("".join(st))
                st=[]
        o=""
        for i in l:
            a=list(i)
            a.pop(0)
            a.pop(-1)
            o+="".join(a)
        return o