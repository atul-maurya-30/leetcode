class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i,j=0,0
        min_l=float('inf')
        s=0
        while j<n:
            s+=nums[j]
            while s>=target:
                min_l=min(min_l,j-i+1)
                s-=nums[i]
                i+=1
            j+=1
        return 0 if min_l==float('inf') else min_l