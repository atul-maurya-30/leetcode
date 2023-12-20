class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_cost = float('inf')
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                cost = prices[i] + prices[j]

                if cost < min_cost:
                    min_cost = cost
        
        if min_cost <= money:
            return money - min_cost
        else:
            return money