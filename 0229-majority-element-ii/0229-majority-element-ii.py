class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        a=[]
        n=len(nums)
        n=n//3
        for k,v in h.items():
            if v>n:
                a.append(k)
        return a