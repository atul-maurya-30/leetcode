class Solution:
    def __init__(self):
        self.l=0
        self.h=0
        self.z=0
        self.o=0
        self.mod=(10**9) + 7

    def solve(self,a,memo):
            if a>self.h:
                return 0
            if memo[a]!+-1:
                return memo[a]

            b=0
            if self.l<=a<=self.h:
                b=1
        
            add_one=self.solve(a+self.o,memo)
            add_zero=self.solve(a+self.z,memo)
            memo[a]=(b+add_one+add_zero)%self.mod
            return memo[a]

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.l=low
        self.h=high
        self.z=zero
        self.o=one
        memo=[-1]*(self.h+1)
        return self.solve(0,memo)
        
        
        