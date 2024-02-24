class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=0
        m=0
        while n<len(s) and m<len(t):
            if s[n]==t[m]:
                n+=1
            m+=1
        return n==len(s)
            
                