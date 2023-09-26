class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        v=set()
        st=[]
        for i,c in enumerate(s):
            if s[i] not in v:
                while st!=[] and c<st[-1] and d[st[-1]]>i:
                    v.remove(st.pop())
                st.append(s[i])
                v.add(s[i])
        return "".join(st)
        
    
        
        
        
        
        
        