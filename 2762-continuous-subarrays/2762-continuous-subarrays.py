class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        #brute force approach
        c=0
        for i in range(len(nums)):
            max_v=nums[i] #initalise max
            min_v=nums[i] #initialise min
            for j in range(i,len(nums)):
                max_v=max(max_v,nums[j]) #
                min_v=min(min_v,nums[j])

                if max_v-min_v<=2: #condtion check
                    c+=1
                else:
                    break
        return c