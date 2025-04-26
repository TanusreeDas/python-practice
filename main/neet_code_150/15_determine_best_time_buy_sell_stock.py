'''You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
Constraints:
1 <= prices.length <= 100
0 <= prices[i] <= 100'''

from time import time
class Solution:
    @staticmethod
    def max_profit_brute_force(prices: list[int]) -> int:
        max_profit = 0
        for i,buy in enumerate(prices):
            for j, sell in enumerate(prices[i+1:]):
                if sell>buy:
                    max_profit = max(max_profit,sell-buy)

        return max_profit

    @staticmethod
    def max_profit_optimized(prices: list[int]) -> int:
        min_sell_price = prices[0]
        max_profit = 0
        for i,price in enumerate(prices):
            if price<min_sell_price:
                min_sell_price=price
            else:
                max_profit=max(max_profit,price-min_sell_price)
        return max_profit


if __name__ == '__main__':
    count = 1
    sol = Solution()
    inputs = [[10,8,7,5,2],[7,1,5,3,6,4],[7,6,4,3,1],[7,2,5,10,4,8,9],[3,3,5,0,0,3,1,4]]
    for num in inputs:
        print(f"Processing input no: {count}")
        start_time = time()
        print(f"Output using brute force generic method: {sol.max_profit_brute_force(num)} and time taken ={time()-start_time} seconds")
        start_time = time()
        print(f"Output using two pointer method: {sol.max_profit_optimized(num)} and time taken ={time()-start_time} seconds")
        print("*"*40)
        count +=1