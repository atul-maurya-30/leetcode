class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        #this is a very easy and optimized approach by use of hashmap
        # as we can count the pattern and save it into map
        h={} 

        #iterate through each row 
        for i in matrix:
            # row="" #string to store th pattern of matrix

            # #for each element in the row ,check if it is same as first element
            # for j in range(len(i)):
            #     #"t" for same ,"f" for flipped
            #     row+="t" if i[0]==i[j] else "f"

            row=tuple(i)
            flip=tuple(1-b for b in i)
            n=min(row,flip)

#update the count in map
            if n in h:
                h[n]+=1
            else:
                h[n]=1
                       
    #return the max values of count in map
        return max(h.values())

 