class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps1 = {}
        maps2 = {}
        maps1 = {i:s.count(i) for i in set(s)}
        maps2 = {i:t.count(i) for i in set(t)}
        return maps1 == maps2