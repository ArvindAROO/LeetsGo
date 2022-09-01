class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sol = 0
        words = [[set(i), len(i)] for i in words]
        # print(words)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i][0].intersection(words[j][0]) == set():
                    sol = max(words[i][1] * words[j][1], sol)
        return sol