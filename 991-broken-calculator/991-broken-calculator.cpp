class Solution {
public:
    int brokenCalc(int startValue, int target) {
        int ans = 0;
        while (target > startValue){
            if (target%2 == 0 && target > startValue) {
                ans++;
                target /= 2;
            } else if (target > startValue) {
                target++;
                ans++;
            } else {
                break;
            }
            
        }
        ans += abs(startValue - target);
        return ans;
    }
};