class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num=sorted(nums)
        s=((num[-2])-1)*((num[-1])-1)
        return s
        