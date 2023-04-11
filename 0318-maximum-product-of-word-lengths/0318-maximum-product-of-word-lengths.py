class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        l=[0]*n
        for i in range(n):
            l[i]=set(words[i])
        m=0
        for i in range(n):
            for j in range(i+1,n):
                if not (l[i]&l[j]):
                    m=max(m,len(words[i])*len(words[j]))
        return m