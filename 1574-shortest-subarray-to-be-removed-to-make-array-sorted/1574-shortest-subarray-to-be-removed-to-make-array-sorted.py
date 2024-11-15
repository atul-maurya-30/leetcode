class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr) #length of array

        #phase-1 find the rightmost pointer "r"  where non decreasing sub array ends
        r=n-1 # r=right
        while r>0 and arr[r]>=arr[r-1]:
            r-=1
        
        l=0 # l=left
        res=r #initialize result as by removing everything upto "r"

        #phase-2 start finding correct left and right pointers and find deleted elements=r-l-1

        while(l<r and (l==0 or arr[l]>=arr[l-1])): 
        #for finding array in increasing order
            #move "r" right to find arr[r]<arr[l]

            while r<n and arr[l]>arr[r]:
                r+=1
            
            #we found correct right position so update left pointer
            res=min(res,r-l-1)
            l+=1 #move "l" to right

        #return the shortest removed subarray length 
        return res