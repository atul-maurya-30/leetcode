class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t=[] #use to store pascal traingle
        for r in range(rowIndex+1): #iteration through rows
            curr_r=[1]*(r+1) #initializing 1's at first and last col in row
            for c in range(1,r): #iteration through columns
                curr_r[c]=t[r-1][c-1]+t[r-1][c] #above sum equal to below sum
            t.append(curr_r) #now to save the current new row in pascal triangle
        return t[-1]