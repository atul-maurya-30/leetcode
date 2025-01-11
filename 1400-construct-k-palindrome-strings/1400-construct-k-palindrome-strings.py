class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c=Counter(s)
        m=0
        for i in c.values():
            if i%2!=0:
                m+=1
        return True if k>=m else False