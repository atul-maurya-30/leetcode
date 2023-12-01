import random
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        c=0
        n={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                key=nums[i]*nums[j]
                if key in n:
                    c+=n[key]
                    n[key]+=1
                else:
                    n[key]=1
        return(c*8)