class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m>n:
            return (m*n)-m
        elif m<n:
            return (m*n)+n
        else:
            return 0

                