class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = [s.count(i) for i in set(s)]
        return all(ele == s[0] for ele in s)