class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c={}
        for i in nums:
            c[i]=c.get(i,0)+1 
        k=0

        for i in c:
            if i+1 in c:
                k=max(k,c[i]+c[i+1])
        return k
