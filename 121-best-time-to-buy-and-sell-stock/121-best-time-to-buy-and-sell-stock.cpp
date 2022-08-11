class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) return 0;
        auto mini = prices[0], profit = 0;
        for(auto i : prices){
            mini = min(mini, i);
            profit = max(profit, i - mini);
            
        }
        return profit;
    }
};