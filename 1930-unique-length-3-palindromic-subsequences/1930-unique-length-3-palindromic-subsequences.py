class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n=len(s)
        k=set(s) 
        
        res=0
        for i in k:
            l=-1
            r=-1
            for j in range(n):
                if s[j]==i:
                    if l==-1:
                        l=j
                    r=j
            m=set()
            for j in range(l+1,r):
                m.add(s[j])
            res+=len(m)
        return res

                

        