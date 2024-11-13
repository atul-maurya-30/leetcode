class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        m=x
        if m<0:
            m=m*(-1)
            c=str(m)
        else:
            c=str(m)
        c=c[::-1]
        c=int(c)
        c=c*sign
        if (-2**31<=c<=((2**31)-1)):
            return c
        else:
            return 0