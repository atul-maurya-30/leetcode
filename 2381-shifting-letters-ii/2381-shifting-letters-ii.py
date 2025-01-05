class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #use of difference array in thi problem
        n=len(s)
        imp=[0]*(n+1) #add extra space to avoid out of range
        for i in shifts:
            a=i[0] #for start
            b=i[1] #for destination
            x=i[2] #for assign task of 0 or 1
            if x==0: #left shift
                imp[a]-=1 #add -1 for bakcward
                if b+1<n: #for checknig out of bound
                    imp[b+1]+=1 #add +1 at after range
            else:#right shift
                imp[a]+=1 #add +1 for forward
                if b+1<n: #for checking of out of bound
                    imp[b+1]-=1 #add -1 at after range
        #cummulative sum for the effiecient last approach
        for i in range(1,n):
            imp[i]=imp[i]+imp[i-1]

        s=list(s)
        for i in range(n):
            value=ord(s[i])-ord("a") #for getting zero based position
            char=(imp[i]+value)%26 #apply shift and wrap around modulo
            s[i]=chr((char)+ord("a")) #convert new position back to character

        #return the string as a result
        return "".join(s)
        
                
