class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                s+=nums[i]
            else:
                s=nums[i]
            m=max(m,s)
        return m