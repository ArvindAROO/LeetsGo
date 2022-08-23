class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {

        int maxi = nums[0], mini = nums[0], l1 = 0, l2 = 0;
        for(auto i : nums){
            l1 += i; l2 += i;
            maxi = max(l1, maxi);
            mini = min(l2, mini);
            if (l1 < 0) l1 = 0;
            if (l2 > 0) l2 = 0;
        }
        return max(maxi, abs(mini));
    }
};