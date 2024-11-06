class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums)==1:
            return nums[0]
        prev_n=0
        prev_r=nums[0]
        for i in range(1,len(nums)):
            s=max(prev_r,prev_n+nums[i])
            prev_n=prev_r
            prev_r=s
        return prev_r
        