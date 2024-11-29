class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=0
        s=0
        m=float('-inf')
        for r in range(len(nums)):
            s+=nums[r]
            m=max(m,s)
            if s<0:
                s=0 #it reset the sum 
                l=r+1
        return m
