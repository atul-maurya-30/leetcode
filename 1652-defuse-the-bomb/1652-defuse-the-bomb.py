class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # i will show you a very easy unique approach
        
        n=len(code)
        if k==0:
            return [0]*n #for handling value == 0
        
        #extend the array for handling circular array
        a=code+code[:-1]
        p=[]
        if k>0:
            for i in range(n):
                s=sum(a[i+1:i+1+k]) #for handling positive value of k
                p.append(s)
        else:
            for i in range(n):
                s=sum(a[n+i+k:n+i]) #for handling negative value of k
                p.append(s)
        return p
