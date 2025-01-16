class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        d=[0]*(n+1)
        d[1]=1
        for i in range(2,n+1):
            d[i]=d[i-1]+d[i-2]
        return d[n]