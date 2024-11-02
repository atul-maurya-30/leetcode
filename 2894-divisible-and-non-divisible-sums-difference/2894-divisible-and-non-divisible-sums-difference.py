class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        o=[]
        for i in range(1,n+1):
            if i %m==0:
                o.append(i)
        return sum(range(1,n+1))-(2*sum(o))