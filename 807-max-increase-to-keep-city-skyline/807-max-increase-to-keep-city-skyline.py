import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        arr = np.array(grid)
        hori = arr.max(axis = 1)
        ver = arr.max(axis = 0)
        del arr
        sol = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sol += min(hori[i], ver[j]) -  grid[i][j]
        return sol