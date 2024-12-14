class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s=0
        if target in nums:
            s=nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i]>=target:
                    return i #insert at postion
            return len(nums) #if larger then every elements then just return last index
        return s #return the s