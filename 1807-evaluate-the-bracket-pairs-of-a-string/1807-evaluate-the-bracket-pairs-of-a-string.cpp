class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        unordered_map<string, string> maps;
        for(auto i : knowledge)
            maps[i[0]] = i[1];
        int i = 0;
        string sol = "";
        while (i < s.size()){
            if (s[i] == '('){
                string temp = "";
                i++;
                while (s[i] != ')'){
                    temp += s[i];
                    i++;
                }
                if (maps.find(temp) != maps.end()){
                    sol += maps[temp];
                } else {
                    sol += "?";
                }
            } else {
                sol += s[i];
            }
            
            i++;
            
        }
        return sol;
    }
};