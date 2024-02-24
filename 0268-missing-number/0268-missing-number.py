class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        nums=sorted(nums)
        b=nums[0:]
        for i in range(len(b)):
            if i != nums[i]:
                return i
        return len(nums)
                
                