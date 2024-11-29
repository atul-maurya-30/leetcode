class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        l=-1
        #step:1 find the first decreasing element(left)
        for i in range(n-2,-1,-1): #traverse from right to left
            if nums[i]<nums[i+1]:
                l=i
                break
        if l!=-1: #if a pivot exists
        #step:2 find the element just larger than nums[left]
            for j in range(n-1,l,-1):
                if nums[j]>nums[l]:
                    #step:3 swap nums[left] and nums[right]
                    nums[l],nums[j]=nums[j],nums[l]
                    break
        nums[l+1:]=reversed(nums[l+1:]) #reverse subarray from left to +1 to the end