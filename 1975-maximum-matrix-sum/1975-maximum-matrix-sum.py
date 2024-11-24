class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

# we have following conditions to fulfil
    #Multiply by -1:
        #Only for two adjacent elements that are adjacent(share a border).
        #We can Choose two maximum absolute values in a row if there are multiple negative no.
    
    #Maximum sum will be return in the last

        t=0 #total sum
        min_abs=float('inf') #this is used to track smallest absolute value of matrix
        n=0 #counter for counting negative no. that are present in matrix
        #traverse through each row of matrix
        for r in matrix:
            #Traverse through each element in row
            for e in r:
                #add abs value of current element(e) to total sum
                t+=abs(e)
                
                #update smallest absolute element seen so far
                min_abs=min(min_abs,abs(e))

                #if the element is negative then increment n by 1
                if e<0:
                    n+=1

        #if there are an odd no. of negative, one will remain same
        #subtract twice the smallest absolute elements to adjust the sum
        if n%2!=0:
            t-=2*min_abs
                    
        #return the maximum sum of the matrix
        return t