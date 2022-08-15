class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        need = max(days)
        for i in range(1, 366):
            if i in days:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
            elif i > need:
                dp[-1] = dp[i - 1]
                break
            else:
                dp[i] = dp[i - 1]
        return dp[-1]