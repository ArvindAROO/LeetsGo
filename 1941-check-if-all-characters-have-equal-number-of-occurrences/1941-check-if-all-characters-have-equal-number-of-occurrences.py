class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = [s.count(i) for i in set(s)]
        return s.count(s[0]) == len(s)