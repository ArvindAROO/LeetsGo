class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, double threshold) {
        int sum = 0;
        for (int i = 0 ; i < k; i++) sum += arr[i];
        int sol = 0;
        if (((double)sum / k) >= threshold) sol ++;
        for (int i = k; i < arr.size(); i++){
            sum -= arr[i-k];
            sum += arr[i];
            if (((double)sum / k) >= threshold) sol++;
        }
        return sol;
    }
};