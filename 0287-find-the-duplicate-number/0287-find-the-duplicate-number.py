class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c=0
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i]==nums[i-1]:
                c=nums[i]
        return c