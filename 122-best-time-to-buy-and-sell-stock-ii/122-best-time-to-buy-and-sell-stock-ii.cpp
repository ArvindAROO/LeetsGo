class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for(int i = 1; i < prices.size(); i++){
            int t = prices[i] - prices[i - 1];
            if (t > 0)
                profit += t;
        }
        return profit;
    }
};