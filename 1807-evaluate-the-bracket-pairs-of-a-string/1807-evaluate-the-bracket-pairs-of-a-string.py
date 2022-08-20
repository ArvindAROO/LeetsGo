class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        i = 0 
        sol = ""
        maps = {j[0]:j[1] for j in knowledge}
        while i < len(s):
            if s[i] == "(":
                i += 1
                copy = i
                temp = ""
                while s[i] != ")":
                    temp += s[i]
                    i+=1
                # print(temp, knowledge)
                if temp in maps:
                    sol += maps[temp]
                else:
                    sol += "?"
            else:
                sol += s[i]
            i+=1
        return sol