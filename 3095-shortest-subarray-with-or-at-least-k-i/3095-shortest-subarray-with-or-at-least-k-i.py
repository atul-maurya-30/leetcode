# class Solution:
#     def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
#         a=float('inf')
#         n=len(nums)
        
#         for i in range(0,n):
#             s,l=0,0
#             for j in range(i,n):
#                 s|=nums[j]
#                 l+=1
#                 if s>=k:
#                     a=min(a,l)
#         return -1 if a==float('inf') else a

class Solution:
    def updatevec(self,number,vec,val):
        for i in range(0,32):
            if (number>>i)&1: #check the ith bit
                vec[i]+=val  #update the count of set bits at the ith position

    def getDecimal(self,vec):
        m=0
        for i in range(0,32):
            if vec[i]>0:  #if there's any set bit in this position
                m|=(1<<i)  #set the ith bit in the result
        return m
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        r=float('inf') #initialize the minimum subarray length as infinity
        vec=[0]*32
        i,j=0,0
        #vec[i]=total no. of setbits in the ith position

        #now we have to follow sliding window technique
        while j<n:
            self.updatevec(nums[j],vec,1) #add current number to the vector
            while i<=j and self.getDecimal(vec)>=k:
                r=min(r,j-i+1) #update the minimum length
                self.updatevec(nums[i],vec,-1) #remove the leftmost number
                i+=1 #shrink the window from the left
            j+=1 #shrink the window from right
        return r if r!=float('inf') else -1 #return the result or -1 if no subarray found