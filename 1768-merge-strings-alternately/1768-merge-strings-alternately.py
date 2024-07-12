class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=""
        m=min(len(word1),len(word2))
        for i,j in zip(word1,word2):
            a+=i+j
        a+=word1[m:]+word2[m:]
        return a