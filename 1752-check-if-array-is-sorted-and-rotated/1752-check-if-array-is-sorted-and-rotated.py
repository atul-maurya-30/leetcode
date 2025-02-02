class Solution:
    def check(self, nums: List[int]) -> bool:
        temp=nums
        for i in range(len(nums)):
            r=temp[i:]+temp[:i]
            if sorted(nums)==r:
                return True
        return False