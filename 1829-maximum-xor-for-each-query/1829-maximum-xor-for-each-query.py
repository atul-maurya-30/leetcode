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

        # totalXor=0
        # for i in nums:
        #     totalXor^=i

        # Calculate the max value with maximumBits
        # maxK=(1<<maximumBit)-1

        # Calculate the result for each query
        # r=[]

        # first way

        # for _ in range(len(nums)):
        #     #k is given as this first query
        #     k=totalXor^maxK
        #     r.append(k)
        #     # totalXor is as second query for removing the element
        #     totalXor^=nums.pop()
        

        #second way
        # for i in reversed(nums):
        #     r.append(totalXor^maxK)
        #     totalXor^=nums.pop()
        # return r

        #third way
        maxK=(1<<maximumBit)-1
        n=len(nums)
        r=[0]*n
        c=0

        for i in range(n):
            c^=nums[i]
            r[n-i-1]=~c&maxK
        return r