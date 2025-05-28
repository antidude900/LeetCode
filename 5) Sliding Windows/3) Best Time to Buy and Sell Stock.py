"""
Approach:
Gives a array of prices where the 'ith' index represents the 'ith' day, we need to find the maximum profit we can get from the transaction.
Here, we use the same sliding window technique but we just values instead of index for the purpose as the process and answer has nothing to do with index.
The simple thing is that if we find a price greater than the price of the current day, we find the new higher profit.
But if the price is less than the price of the current day, we take that as the start of our window as buying from more lower price will obviously be nice than buying from higher price.
Also we dont have to worry abou the past values as we cannot sell our bought stock in the past day!
"""

def maxProfit(prices: List[int]) -> int:
    leftVal = prices[0]
    max_profit = 0
    for rightVal in prices:
        if rightVal < leftVal:
            leftVal = rightVal
        elif rightVal-leftVal > max_profit:
            max_profit = rightVal-leftVal
    return max_profit
    
