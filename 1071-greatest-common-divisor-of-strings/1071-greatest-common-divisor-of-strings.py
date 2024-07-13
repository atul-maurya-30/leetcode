class Solution:
    def gcd(self,a,b):
        if a==0:
            return b
        else:
            return self.gcd(b%a,a)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        else:
            return str1[:gcd(len(str1),len(str2))]