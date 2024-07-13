class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        s=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m:
                s.append(True)
            else:
                s.append(False)
        return s