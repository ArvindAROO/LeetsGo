class Solution:
    def shortestToChar(self, s: str, char: str) -> List[int]:
        indices = [i for i, c in enumerate(s) if c == char]
        return [min([abs(j - i) for j in indices]) for i in range(len(s))]