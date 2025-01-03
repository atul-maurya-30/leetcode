class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #we use prefix sum for fast computation
        pre_sum=[0]*len(nums) #intialize prefix_sum array
        pre_sum[0]=nums[0] #set the first prefix_sum value

        #compute prefix_sum
        for i in range(1,len(nums)):
            pre_sum[i]=pre_sum[i-1]+nums[i]

        c=0 #counter for valid splits
        for i in range(len(nums)-1): #iterate and count valid splits
            left=pre_sum[i] #left sum
            right=pre_sum[-1]-pre_sum[i] #right sum
            if left>=right: #condtion for valid split
                c+=1 #increment counter
                
        return c #return result