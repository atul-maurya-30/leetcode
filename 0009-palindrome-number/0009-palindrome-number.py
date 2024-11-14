class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        c=s[::-1]
        return c==s