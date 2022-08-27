class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for(auto i : words){
            string copy = i;
            reverse(i.begin(), i.end());
            if(copy == i)
                return i;
        }
        return "";
    }
};