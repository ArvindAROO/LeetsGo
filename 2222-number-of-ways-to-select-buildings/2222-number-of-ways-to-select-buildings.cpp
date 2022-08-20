class Solution {
public:
    long long numberOfWays(string s) {
        long c0 = 0, c1 = 0, c10 = 0, c01 = 0, c101 = 0, c010 = 0;
        for (auto i : s){
            if(i == '0'){
                c0++;
                c10 += c1;
                c010 += c01;
            } else {
                c1++;
                c01 += c0;
                c101 += c10;
            }
        }
        return c101 + c010;
    }
};