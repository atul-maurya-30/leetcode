class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        b=set()
        for i in nums:
            if i in b:
                return True
            b.add(i)
        return False