class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=Counter(nums)
        for i,k in n.items():
            if k==1:
                return i