class Solution:
    def poss(self,m,piles,n):
        s=0
        for i in piles:
            s+=(i+m-1)//m
            if s>n:
                return True
        return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            m=(l+r)//2
            if self.poss(m,piles,h):
                l=m+1
            else:
                r=m
        return l