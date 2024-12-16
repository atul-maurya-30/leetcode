class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            m=min(nums)
            ind=nums.index(m)
            nums[ind]=nums[ind]*multiplier
        return nums