class Solution:
    def countVowelStrings(self, n: int) -> int:
        k=5+n-1
        sn=1
        snr=1
        sr=1
        for i in range(1,k+1):
            sn*=i
        for i in range(1,k-n+1):
            snr*=i
        for i in range(1,n+1):
            sr*=i
        return sn//(sr*snr)
        
        
        