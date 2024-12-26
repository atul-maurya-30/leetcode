class Solution:
    #brute force but time limit exceeded but can be run in the C++
    # def solve(self,nums,i,s,target):
    #     if i==len(nums):
    #         if s==target:
    #             return 1
    #         return 0
    #     plus=self.solve(nums,i+1,s+nums[i],target)
    #     minus=self.solve(nums,i+1,s-nums[i],target)
    #     return plus+minus

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     return self.solve(nums,0,0,target)


    #using hash map
    def solve(self,nums,i,s,target,h):
        if i==len(nums):
            if s==target:
                return 1
            return 0
        k=f"{i}_{s}" #create unique key for current state
        
        if k in h: #create if result is already save in hashmap
            return h[k]

        #compute result recusively
        plus=self.solve(nums,i+1,s+nums[i],target,h)
        minus=self.solve(nums,i+1,s-nums[i],target,h)

        #store result in hashmap as memoization
        h[k]=plus+minus
        return h[k] #return result
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        h={}
        return self.solve(nums,0,0,target,h)