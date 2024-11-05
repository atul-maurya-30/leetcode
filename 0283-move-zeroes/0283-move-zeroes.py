class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        s=[0]*nums.count(0)
        nums[:]=[num for num in nums if num!=0]
        nums.extend(s)
        
