class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        #for 2 no.
        if l<=2:
            return nums.reverse()
        #for more than 2 no. and check for pointer "p"
        p=l-2
        while p>=0 and nums[p]>=nums[p+1]:
            p-=1
        #if the element is last
        if p==-1:
            return nums.reverse()
        #as per use of pointer swap the elements 
        for i in range(l-1,p,-1):
            if nums[p]<nums[i]:
                nums[p],nums[i]=nums[i],nums[p]
                break
        nums[p+1:]=reversed(nums[p+1:])
        return nums
                