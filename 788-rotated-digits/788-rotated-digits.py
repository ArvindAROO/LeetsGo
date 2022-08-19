class Solution:
    def rotatedDigits(self, n: int) -> int:
        sol = 0
        for i in range(1, n + 1):
            temp = set(str(i))
            # print(temp)
            # if len(temp) == 1:
            if set("180").union(temp) == set("180"):
                continue
            if set("2569180").union(temp) == set("2569180"):
                sol += 1
        return sol