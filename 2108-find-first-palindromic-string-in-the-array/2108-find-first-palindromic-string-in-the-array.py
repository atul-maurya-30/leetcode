class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            r="".join(reversed(i))
            if i==r:
                return i
        return ""
                