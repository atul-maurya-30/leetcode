class Solution:
    def rob(self, nums: List[int]) -> int:
        r,nr=0,0
        for i in nums:
            newr=nr+i
            newnr=max(nr,r)
            r,nr=newr,newnr
        return max(r,nr)