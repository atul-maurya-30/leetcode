class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        max_m=float("-inf")
        for i in range(1,n):
            left=s[:i]
            right=s[i:]

            z=left.count("0")
            o=right.count("1")
            max_m=max(max_m,o+z)
        return max_m