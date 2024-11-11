class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)
        m=n//2
        v=[]
        a=nums[:m]
        b=nums[m:]
        for i in range(m):
            v.append(a[i])
            v.append(b[i])
        
        return v