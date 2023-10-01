class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if(n==1):
            return([[1]])
        elif(n==2):
            return([[1],[1,1]])
        else:
            k=[[1],[1,1]]
            for i in range(3,n+1):
                l=[1]
                for i in range(len(k[-1])-1):
                    l.append(k[-1][i]+k[-1][i+1])
                l.append(1)
                k.append(l)
            return k
                
                
        