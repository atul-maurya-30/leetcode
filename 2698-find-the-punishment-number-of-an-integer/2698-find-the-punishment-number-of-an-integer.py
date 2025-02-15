class Solution:
    def check(self,i,currsum,sq,curr):
        if i==len(sq):
            return currsum==curr #if all digits are processed, check if sum matches

        if currsum>curr: 
            return False

        pos=False
        for j in range(i,len(sq)):
            sub=sq[i:j+1] #substrings check
            val=int(sub) #change datatype
            pos=pos or self.check(j+1,currsum+val,sq,curr)
            if pos==True:
                return True
        return pos
    def punishmentNumber(self, n: int) -> int:
        s=0 #sum
        for curr in range(1,n+1):
            sq=str(curr**2) #square of no.
            
            #if square no. can be partitioned to sum to the original no., add to sum
            if self.check(0,0,sq,curr):
                s+=curr**2
        return s