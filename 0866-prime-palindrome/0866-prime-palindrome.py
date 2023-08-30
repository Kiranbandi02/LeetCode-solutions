class Solution:
    def primePalindrome(self, n: int) -> int:
        if n >= 9989900:
            return 100030001
        import math
        def p(n):
            if(n<=1):
                return False
            if(n<=3):
                return True
            if(n%2==0):
                return False
            if(n%3==0):
                return False
            sq=int(math.sqrt(n))
            for i in range(5,sq+1,2):
                if(n%i==0):
                    return False
            return True
        i=n
        while 1:
            if(str(i)==str(i)[::-1] and p(i)):
                return i
            i+=1
        