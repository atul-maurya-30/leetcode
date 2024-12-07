class Solution:
    #helper function to check for that elements are possble to reduce elements  
    def ifpossible(self,nums,m,mid):
        o=0 #total operation required
        for i in nums:
            #cal the no. of operations needed to make num<mid
            s=i//mid #no. of parts created by dividing i
            if i%mid==0: #if divisble,reduce one operation
                s-=1
            o+=s#add total operation
        #if the total in bound of m then return True
        return o<=m
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l=1 #smallest possible no.
        r=max(nums) #largest no. 
        result=0 #result
        #binary search applied
        while l<=r:
            mid=l+(r-l)//2
            if self.ifpossible(nums,maxOperations,mid):
                result=mid
                r=mid-1
            else:
                l=mid+1
        return result