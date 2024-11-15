class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                l=nums[:i]+nums[j:]
                if l==sorted(l) and len(l)==len(set(l)):
                    c+=1
        return c