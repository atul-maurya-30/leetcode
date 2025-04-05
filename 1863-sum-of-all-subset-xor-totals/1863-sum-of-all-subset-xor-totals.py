class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        r=0 #to store cummulative or of all no.

        # iterate through each no. in the arr
        for n in nums:
            #perform bitwise OR operation ,this ensures that all bits present in no. are inlcuded in r
            r|=n

        # multiply by subset count contribution
        return r*(2**(len(nums)-1))