class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        h1={}
        for i in word1:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        h2={}
        for i in word2:
            if i in h2:
                h2[i]+=1
            else:
                h2[i]=1
        if sorted(h1.values())==sorted(h2.values()) and set(h1.keys())==set(h2.keys()):
            return True
        return False
