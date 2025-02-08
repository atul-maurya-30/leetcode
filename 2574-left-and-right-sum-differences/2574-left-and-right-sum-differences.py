class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s=0
        l=[0]
        for i in range(0,len(nums)-1):
            s+=nums[i]
            l.append(s)
        s=sum(nums[1:len(nums)+1])
        r=[s]
        for i in range(1,len(nums)):
            s-=nums[i]
            r.append(s)
        
        a=[]
        for i in range(len(nums)):
            k=abs(l[i]-r[i])
            a.append(k)
        return a