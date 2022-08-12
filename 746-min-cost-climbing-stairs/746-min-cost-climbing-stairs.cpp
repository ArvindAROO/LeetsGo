class Solution {
public:
    
    int minCostClimbingStairs(vector<int>& cost) {
        auto n = (int)cost.size();
        vector<int> dp(n, 0);
        if (n == 1) return cost[0];
        if (n == 2) return min(cost[0], cost[1]);
        dp[n - 1] = cost[n - 1];
        dp[n - 2] = cost[n - 2];
        for (int i = n-3; i >= 0; i--){
            dp[i] = min(dp[i + 1] + cost[i], dp[i + 2] + cost[i]);
        }
        return min(dp[0], dp[1]);
    }
};