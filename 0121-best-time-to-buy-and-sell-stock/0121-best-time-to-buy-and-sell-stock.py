class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k=prices[0]
        pro=0
        for i in range(1,len(prices)):
            if prices[i]<k:
                k=prices[i]
            elif prices[i]-k>pro:
                pro=prices[i]-k
        return pro
        