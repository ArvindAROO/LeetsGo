class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start > goal:
            bin1 = bin(start)[2:]
            bin2 = bin(goal)[2:].zfill(len(bin1))
        elif start < goal:
            bin2 = bin(goal)[2:]
            bin1 = bin(start)[2:].zfill(len(bin2))
        else:
            return 0
        sol = 0
        for i in range(len(bin1)):
            if bin1[i] != bin2[i]:
                sol += 1
        return sol