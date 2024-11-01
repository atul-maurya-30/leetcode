class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        c=0
        for i in range(n):
            m=nums[i]%3
            if m==0:
                continue
            else :
                c+=1
        return c