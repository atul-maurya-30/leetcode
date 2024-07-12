class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=""
        m=min(len(word1),len(word2))
        for i in range(m):
            a+=word1[i]+word2[i]
        a+=word1[m:]+word2[m:]
        return a