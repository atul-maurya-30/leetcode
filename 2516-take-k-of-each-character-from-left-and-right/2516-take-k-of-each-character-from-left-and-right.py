class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n=len(s)
       #first we count all the elements in string as per a,b,c.
        c_a=c_b=c_c=0
        for char in s:
            if char=="a":
                c_a+=1
            elif char=="b":
                c_b+=1
            elif char=="c":
                c_c+=1
        if (c_a<k or c_b<k or c_c<k):
            return -1  #not possible to del k characters
        delete=0
        i=0
        j=0
        while j<n:
            if s[j]=="a":
                c_a-=1
            elif s[j]=="b":
                c_b-=1
            else:
                c_c-=1

            #if deletion count of any char becomes less than k then just shrink the window

            while (i<=j) and (c_a<k or c_b<k or c_c<k):
                #left pointer move to left
                if s[i]=="a":
                    c_a+=1
                elif s[i]=="b":
                    c_b+=1
                else:
                    c_c+=1
                i+=1
            delete=max(delete,j-i+1)
            j+=1
        return n-delete
