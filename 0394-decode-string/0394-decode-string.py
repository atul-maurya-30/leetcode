class Solution:
    def decodeString(self, s: str) -> str:
        h=[]
        o=""
        n=0

        for c in s:
            if c.isdigit():
                #for handling multi-digit no.
                n=n*10+int(c)
            elif c=="[":
                #push in stack
                h.append((o,n))
                o,n="",0 #reset initial variables
            elif c=="]":
                # pop from stack 
                p,m=h.pop()
                o=p+o*m #applu string mulipication in it 
            else:
                o+=c #append the character
        return o