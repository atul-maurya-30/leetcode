class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        # Xor all the elements to get the cumulative XOR
            # y Xor 0= y (different)
            # y Xor y= 0 (same)

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
        # maxK=(1<<maximumBit)-1
        # n=len(nums)
        # r=[0]*n
        # c=0

        # for i in range(n):
        #     c^=nums[i]
        #     r[n-i-1]=~c&maxK
        # return r


        #fourth way
        n=len(nums)
        r=[]
        x=0
        for i in range(n):
            x^=nums[i]

        maxk=((1<<maximumBit)-1) #it works as 2^n-1

        for i in range(n):
            k=x^maxk #this will give the flipped value of Xor i.e. for best k
            r.append(k)
            x=(x^nums[n-1-i])
        return r
