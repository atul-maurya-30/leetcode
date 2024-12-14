class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using floyd tortoise hare algorithm
        #phase 1: detect duplicate
        s=nums[0] #slow pointer
        f=nums[0] #fast pointer

        # move slow by 1 step and and fast by 2 steps
        
        while True:
            s=nums[s]
            f=nums[nums[f]]
            if s==f: 
                break #duplicate found
        #phase 2: find the duplicate
        s=nums[0] #move slow to start
        while s!=f:
            s=nums[s] #by 1 step
            f=nums[f]  #by 1 step
        return f #final no. 