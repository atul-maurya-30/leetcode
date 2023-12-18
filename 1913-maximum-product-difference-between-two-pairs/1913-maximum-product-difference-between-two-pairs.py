class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        m=sorted(nums,reverse=True)
        max_a=m[0]
        max_b=m[1]
        n=sorted(nums)
        min_c=n[0]
        min_d=n[1]
        s=(max_a*max_b)-(min_c*min_d)
        return(s)