class Solution {
public:
    vector<int> twoSum(vector<int>& vec, int target) {
        // vector<int> sol = {};
        int i = 0, j;
        for(auto it1 = vec.begin(); it1 != vec.end(); it1++){
            j = 0;
            for(auto it2 = vec.begin(); it2 != vec.end(); it2++){
                if ((i != j) && (*it1 + *it2 == target)){
                    // cout << "lmao";
                    return vector<int>{i,j};
                }
                ++j;
            }
            ++i;
        }
        return vector<int>(0,0);
    }
};