class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        buy = 0
        sell = 1
        profit  = 0
        max_profit = profit
        while sell < len(nums):
            
            if nums[sell]-nums[buy] <= 0:
                buy = sell
                sell = buy + 1
                
            else:
                if nums[sell]-nums[buy] > profit:
                    profit = nums[sell]-nums[buy]
                sell += 1
        return profit
            