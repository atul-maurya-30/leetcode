class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        if l<=2:
            return nums.reverse()
        p=l-2
        while p>=0 and nums[p]>=nums[p+1]:
            p-=1
            
        if p==-1:
            return nums.reverse()
        for i in range(l-1,p,-1):
            if nums[p]<nums[i]:
                nums[p],nums[i]=nums[i],nums[p]
                break
        nums[p+1:]=reversed(nums[p+1:])
                