class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        sol = []
        curr = 0
        for i in range(m):
            sol.append(original[curr:curr + n])
            curr += n
        return sol