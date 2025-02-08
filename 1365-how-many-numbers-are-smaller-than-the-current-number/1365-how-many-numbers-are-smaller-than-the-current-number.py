class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[i]>nums[j] and i!=j:
                    c+=1
            k.append(c)
        return k
                