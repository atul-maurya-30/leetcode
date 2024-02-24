class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=(n*(n+1))/2
        m=sum(nums)
        return int(total-m)