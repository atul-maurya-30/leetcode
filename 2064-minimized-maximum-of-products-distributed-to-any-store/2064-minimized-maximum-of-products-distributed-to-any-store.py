class Solution:
    def poss(self,mid,quantities,n):
        s=0
        for i in quantities:
            s+= (i+mid-1)//mid #like ciel funstion
            if s>n:
                return True
        return s>n

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l=1
        r=max(quantities)
        while(l<r):
            mid=(l+r)//2
            if self.poss(mid,quantities,n):
                l=mid+1
            else:
                r=mid
        return l