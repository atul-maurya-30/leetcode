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
    def solve(self,nums,i,s,target,h):
        if i==len(nums):
            if s==target:
                return 1
            return 0
        k=f"{i}_{s}"
        if k in h:
            return h[k]
        plus=self.solve(nums,i+1,s+nums[i],target,h)
        minus=self.solve(nums,i+1,s-nums[i],target,h)
        return plus+minus
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        h={}
        return self.solve(nums,0,0,target,h)