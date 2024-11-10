class Solution:
    def updatevec(self,number,vec,val):
        for i in range(0,32):
            if (number>>i)&1:
                vec[i]+=val

    def getDecimal(self,vec):
        m=0
        for i in range(0,32):
            if vec[i]>0:
                m|=(1<<i)
        return m
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        r=float('inf')
        vec=[0]*32
        i,j=0,0
        #vec[i]=total no. of setbits in the ith position

        #now we have to follow sliding window technique
        while j<n:
            self.updatevec(nums[j],vec,1)
            while i<=j and self.getDecimal(vec)>=k:
                r=min(r,j-i+1)
                self.updatevec(nums[i],vec,-1)
                i+=1
            j+=1
        return r if r!=float('inf') else -1