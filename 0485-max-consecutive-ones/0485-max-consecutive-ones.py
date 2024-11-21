class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        w=0
        m=0
        for r in range(n):
            if nums[r]==1:
                w+=1
            elif nums[r]==0:
                w=0
            m=max(w,m)
        return m