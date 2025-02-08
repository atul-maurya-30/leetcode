class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        s=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]<target and i<j:
                    s+=1
        return s