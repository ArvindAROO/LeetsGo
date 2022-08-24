class Solution {
public:
    int mem[60];
    int recur(int n){
        if (n == 0) return 1;
        if (mem[n] != -1) return mem[n];
        int ans = INT_MIN;
        for(int i = 1; i <= n; i++){
            ans = max(ans, i * recur(n - i));
        }
        mem[n] = ans;
        return ans;
    }
    int integerBreak(int n) {
        if (n == 2 || n == 3) return n - 1;
        memset(mem, -1, sizeof mem);
        return recur(n);
    }
};