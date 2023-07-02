class Solution:
    def largestOddNumber(self, num: str) -> str:
        if(int(num[-1])%2!=0):
            return num
        m=0
        c=""
        for i in num:
            c+=i
            if(int(c[-1])%2!=0):
                m=max(str(m),c)
        if(m==0):
            return ""
        return str(m)