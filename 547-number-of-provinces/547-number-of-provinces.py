class Solution:
    def dfs(self, curr):
        for i in range(len(self.grid[curr])):
            if self.grid[curr][i] == 1:
                if i not in self.visited:
                    self.visited.append(i)
                    self.notYet.remove(i)
                    self.dfs(i)
        
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.grid = isConnected
        self.visited = []
        self.notYet = [i for i in range(len(self.grid))]
        count = 0
        while self.notYet:
            count += 1
            self.dfs(self.notYet[0])
        # print(self.visited, self.notYet)
        return count