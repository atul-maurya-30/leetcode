class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        amax=bmin=bmax=a_count=0
        for i in nums:
            c_count=bin(i).count('1')
            if a_count==c_count:
                bmin=min(bmin,i)
                bmax=max(bmax,i)
            elif bmin<amax:
                return False
            else:
                amax=bmax
                bmin=bmax=i
                a_count=c_count
        return bmin>=amax