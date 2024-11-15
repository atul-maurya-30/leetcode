class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)

        #phase-1 find the jth pointer from the right side
        r=n-1
        if arr==sorted(arr):
            return 0
        while r>0 and arr[r]>=arr[r-1]:
            r-=1
        
        l=0
        res=n

        #phase-2 start finding correct left and right pointers and find delted elements=r-l-1

        while(l<r and (l==0 or arr[l]>=arr[l-1])): #for finding array in incraseing order
            #arr[r]<arr[l]
            while r<n and arr[l]>arr[r]:
                r+=1
            
            #we found correct right pos
            res=min(res,r-l-1)
            l+=1
        return res