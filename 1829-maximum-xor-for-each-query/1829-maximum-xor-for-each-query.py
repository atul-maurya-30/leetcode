class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        # Xor all the elements to get the cumulative XOR
            # xXor0=0 (different)
            # xXorx=x (same)
        totalXor=0
        for i in nums:
            totalXor^=i

        # Calculate the max value with maximumBits
        maxK=(1<<maximumBit)-1

        # Calculate the result for each query
        r=[]
        for _ in range(len(nums)):

            #k is given as this first query
            k=totalXor^maxK
            r.append(k)

            # totalXor is as second query for removing the element
            totalXor^=nums.pop()
        return r