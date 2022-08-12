class Solution:
    def longestPalindrome(self, s: str) -> int:
        maps = {}
        for i in s:
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1
        evenCounts = []
        oddCounts = []
        for i in maps.values():
            if i & 1:
                oddCounts.append(i)
            else:
                evenCounts.append(i)
        sol = sum(evenCounts)
        print(oddCounts)
        for i in oddCounts:
            sol += i - 1
        if len(oddCounts) != 0:
            return sol + 1
        return sol