class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x=0
        y=0
        s="".join(map(str,nums))
        for i in range(len(nums)):
            x=x+nums[i]
        for j in s:
            y+=int(j)
        return abs(x-y)