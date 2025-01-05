class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n=len(s)
        r=shifts[::-1]
        for i in range(1,len(r)):
            r[i]+=r[i-1]
        k=r[::-1]
        s=list(s)
        for i in range(n):
            v=ord(s[i])-ord("a")
            z=(v+k[i])%26
            s[i]=chr(z+ord("a"))
        return "".join(s)

