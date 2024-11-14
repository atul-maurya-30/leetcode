class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p=float("inf")
        max_p=0

        for price in prices:
            if price<min_p:
                min_p=price
            pro=price-min_p
            if pro>max_p:
                max_p=pro
        return max_p