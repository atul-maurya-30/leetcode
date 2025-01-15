class Solution:
    def isset(self,x,b):
        #check if the b-th bit in x is set
        return x&(1<<b)
    
    def setbit(self,x,b):
        #set the b-th bit
        return x|(1<<b)

    def unsetbit(self,x,b):
        #unset the b-th bit
        return x&~(1<<b)

    def minimizeXor(self, num1: int, num2: int) -> int:
        x=num1
        req=bin(num2).count("1") #required 1-bits (from num2)
        curr=bin(x).count("1") #current 1-bits in num1

        if curr<req:
            #add bit to match with the required count
            b=0
            while(curr<req):
                if not self.isset(x,b): # if unset then we need to set the bit
                    x=self.setbit(x,b) #set bit
                    curr+=1
                b+=1
            
        elif curr>req:
            #remove bits to match the required count
            b=0
            while(curr>req):
                if self.isset(x,b): #if bit is set then we need to unset the bit
                    x=self.unsetbit(x,b) #unset the bit
                    curr-=1
                b+=1
        
        return x