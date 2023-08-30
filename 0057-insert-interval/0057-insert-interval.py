class Solution:
    def insert(self, intervals: List[List[int]], n: List[int]) -> List[List[int]]:
        st=[]
        f=0
        for i in intervals:
            if(f==0):
                if(n[0]<i[0] and n[1]<i[0]):
                    st.append(n)
                    st.append(i)
                    f=1
                elif(i[0]>=n[0] and i[1]<=n[1]):
                    st.append([min(i[0],n[0]),max(i[1],n[1])])
                    f=1
                elif(i[0]>=n[0] and i[1]>=n[1]):
                    st.append([min(i[0],n[0]),max(i[1],n[1])])
                    f=1
                elif(i[0]>=n[0] and i[1]<=n[0]):
                    st.append([min(i[0],n[0]),max(i[1],n[1])])
                    f=1
                elif(i[0]<=n[0] and i[1]>=n[0]):
                    st.append([min(i[0],n[0]),max(i[1],n[1])])
                    f=1
                else:
                    st.append(i)
            else:
                k=st[-1]
                if(k[0]<=i[0] and k[1]>=i[0]):
                    print(st)
                    st.pop()
                    st.append([min(i[0],k[0]),max(i[1],k[1])])
                else:
                    st.append(i)
        if(f==0):
            st.append(n)
        return st
        
            
            
            
            
            
            
        