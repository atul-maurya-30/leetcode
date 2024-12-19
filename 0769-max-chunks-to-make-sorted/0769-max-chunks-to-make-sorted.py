class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        #create prefixmax and suffixmin
        pre=arr[:]
        suf=arr[:]

        #calculate prefix maximum    
        for i in range(1,n):
            pre[i]=max(pre[i],pre[i-1])
        
        #calculate suffix minimum
        for i in range(n-2,-1,-1):
            suf[i]=min(suf[i],suf[i+1])

        #count the no. of chunks
        c=0
        for i in range(n):
            #if there are no elements to the left,pre[i-1] is irrelevant
            bef_max=pre[i-1] if i>0 else -float('inf')
            aft_min=suf[i]
            if bef_max<=aft_min:
                c+=1
        return c
                