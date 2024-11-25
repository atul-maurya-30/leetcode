class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        r=0
        for n in nums:
            r|=n
        return r*(2**(len(nums)-1))