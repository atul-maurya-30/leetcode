class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        totalXor=0
        for i in nums:
            totalXor^=i
        maxK=(1<<maximumBit)-1

        r=[]
        for _ in range(len(nums)):
            k=totalXor^maxK
            r.append(k)

            totalXor^=nums.pop()
        return r