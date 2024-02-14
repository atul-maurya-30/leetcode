class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def sub(arr,left,right):
            if left==right:
                return arr[left]
            mid=(left+right)//2
            left_max=sub(arr,left,mid)
            right_max=sub(arr,mid+1,right)
            maxim=self.Sum(arr,left,right,mid)
            return max(maxim,left_max,right_max)
        return sub(nums,0,len(nums)-1)
    def Sum(self,arr,left,right,mid):
        left_sum=float('-inf')
        curr=0
        for i in range(mid,left-1,-1):
            curr+=arr[i]
            left_sum=max(left_sum,curr)
        right_sum=float('-inf')
        curr=0
        for i in range(mid+1,right+1):
            curr+=arr[i]
            right_sum=max(right_sum,curr)
        return left_sum+right_sum