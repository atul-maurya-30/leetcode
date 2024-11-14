class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p=float("inf")
        max_p=0

#like we use min or max
        for price in prices:
            if price<min_p: 
                min_p=price #update the min value

            pro=price-min_p #update the profit

            if pro>max_p: 
                max_p=pro #update the max value
        return max_p