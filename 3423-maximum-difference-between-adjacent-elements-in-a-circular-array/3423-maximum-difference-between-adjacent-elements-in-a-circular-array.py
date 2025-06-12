class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        s=0
        m=float(-inf)
        nums.append(nums[0])
        for i in range(1,len(nums)):
            s=abs(nums[i-1]-nums[i])
            m=max(m,s)
        return m