class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        #its like a brute force approach with a tricky logic i.e.
        #we just have to find the rows that is equal to current rows
        # or inverted flips of that rows.
        
        m=0 #max=0
        for i in range(len(matrix)): #outer loop (base rows)
            r=0 #reset the value of r everytime
            for j in range(len(matrix)): #inner loop (comaring rows with each other)
            #condition 1: rows are already identical
            #condition 2: rows can be made identical by flipping all columns
                if matrix[i]==matrix[j] or matrix[i]==[1-bit for bit in matrix[j]]:
                    r+=1 #increment the value of counter
            m=max(m,r) #max value of r
        return m