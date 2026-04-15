class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        # left and right
        l=r=0
        # min price
        minPrice=prices[l]
        while r<len(prices)-1:
            r+=1
            print(f'right at {r}, left at {l}')
            profit = max(profit,prices[r]-prices[l])
            minPrice=min(minPrice,prices[l])
            while l<r and minPrice>prices[r]:
                l=r
                profit = max(profit,prices[r]-prices[l])

        return profit