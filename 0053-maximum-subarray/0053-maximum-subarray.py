class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we use sliding window approach in it
        # l=0
        # s=0
        # m=float('-inf')
        # for r in range(len(nums)):
        #     s+=nums[r]
        #     m=max(m,s)
        #     if s<0:
        #         s=0 #it reset the sum 
        #         l=r+1
        # return m

#kadane algo
        s=0
        m=float("-inf")
        for i in nums:
            s+=i
            m=max(m,s)
            if s<0:
                s=0
        return m
            