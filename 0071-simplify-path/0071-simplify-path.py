class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        #if(path=="/..." or path=="/.../"):
           # return "/..."
        s=path.split("/")
        for i in s:
            if(i!="." and i!=".."  and i!=""):
                st.append(i)
            if(i==".."):
                if(st!=[]):
                    st.pop(-1)
        if(st==[]):
            return "/"
        k="/"+"/".join(st)
        return k
                