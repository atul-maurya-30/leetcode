class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        c=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        for i in range(len(nums)//2):
            c.append(a[i])
            c.append(b[i])
        return c