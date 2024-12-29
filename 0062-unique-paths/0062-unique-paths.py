class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #total moves required are m-1 down moves and n-1 right moves
        #combination formula C(m+n-2,m-1), compute the no. of ways to arrange these moves
        return math.comb(((m-1)+(n-1)),n-1) #can use any one (m-1)/(n-1)
                