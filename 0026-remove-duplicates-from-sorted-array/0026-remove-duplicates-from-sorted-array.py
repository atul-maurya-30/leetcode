class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique=list(set(nums))
        unique.sort()
        nums[:]=unique
        return len(nums)