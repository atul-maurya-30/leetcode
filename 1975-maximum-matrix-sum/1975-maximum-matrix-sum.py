class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

# we have following conditions to fulfil
    #Multiply by -1:
        #Only for two adjacent elements that are adjacent(share a border).
        #We can Choose two maximum absolute values in a row if there are multiple negative no.
    
    #Maximum sum will be return in the last

        t=0
        min_abs=float('inf')
        n=0
        for i in matrix:
            for val in i:
                t+=abs(val)
                min_abs=min(min_abs,abs(val))
                if val<0:
                    n+=1
        if n%2!=0:
            t-=2*min_abs
                    
        return t