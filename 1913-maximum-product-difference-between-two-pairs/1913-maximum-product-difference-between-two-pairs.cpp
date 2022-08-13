class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        sort(nums.begin(), nums.end());
//         cout << * nums.end() << endl;
//         cout << * (nums.end() - 1) << endl;
        
//         cout << * (nums.end() - 2) << endl;
//         return 1;
        return ( * (nums.end() - 2) * *(nums.end() - 1)) - (nums[0] * nums[1]);
    }
};