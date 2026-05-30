# T: O(n), S: O(1)
class Solution:
    def max_profit(self, prices: list[int]) -> int:
        profit = 0
        p1 = 0
        p2 = p1 + 1
        n = len(prices)

        while p2 < n:
            curr_profit = 0
            if prices[p1] < prices[p2]:
                curr_profit = prices[p2] - prices[p1]
                profit = max(profit, curr_profit)
                p2 += 1

            elif prices[p1] >= prices[p2]:
                p1 = p2
                p2 += 1

        return profit


prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.max_profit(prices))
