class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p=1 #store the product of left
        s=1 #store the product of right
        r=[0]*n #null list
        for i in range(n):
            r[i]=p  #set the current index to the product of left
            p*=nums[i] #update p
        for i in range(n-1,-1,-1):
            r[i]*=s #multiply current value by the product of right 
            s*=nums[i] #update s
        return r