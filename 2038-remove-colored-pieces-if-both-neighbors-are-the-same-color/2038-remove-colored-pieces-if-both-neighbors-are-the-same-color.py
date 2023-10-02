class Solution:
    def winnerOfGame(self, c: str) -> bool:
        st=[]
        a=0
        b=0
        for i in range(1,len(c)-1):
            if(c[i-1]==c[i]==c[i+1] and c[i]=="A"):
                a+=1
            elif(c[i-1]==c[i]==c[i+1] and c[i]=="B"):
                 b+=1
                 
        return a-b>=1
                    