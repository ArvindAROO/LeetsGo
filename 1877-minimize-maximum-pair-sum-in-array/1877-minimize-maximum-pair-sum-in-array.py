class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int maxi = 0, local;
        for(int i = 0; i < n / 2; i++){
            maxi  = max(maxi, nums[i] + nums[n - i - 1]);
                // maxi = local;
        }
        return maxi;
    }
};