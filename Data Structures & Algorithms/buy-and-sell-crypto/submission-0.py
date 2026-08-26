class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, left, right = 0, 0, 1
        while right < len(prices):
            curr = prices[right]-prices[left]
            if curr > 0:
                max_profit = max(max_profit, curr)
            else:
                left = right
            right +=1
        return max_profit

        
            

