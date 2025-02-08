class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=[]
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            s.append(c)
        return s