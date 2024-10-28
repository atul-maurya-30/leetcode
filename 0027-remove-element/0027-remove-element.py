class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c=0
        n=len(nums)
        while val in nums:
            nums.remove(val)
            c+=1
        return n-c
            