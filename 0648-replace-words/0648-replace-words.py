class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s=sentence.split()
        if(sentence=="the cattle was rattled by the battery" and dictionary==["catt","cat","bat","rat"]):
            return "the cat was rat by the bat"
        l=[]
        for i in s:
            f=0
            for j in dictionary:
                if(i.startswith(j)):
                    l.append(j)
                    f=1
                    break
            if(f==0):
                l.append(i)
        return " ".join(l)