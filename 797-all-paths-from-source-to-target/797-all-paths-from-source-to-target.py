class Solution:
    def dfs(self, sofar):
        # print(sofar[-1])
        if sofar[-1] == self.target:
            self.sol.append(sofar)
            return
        else:
            for i in self.graph[sofar[-1]]:
                # sofar.append(i)
                self.dfs(sofar + [i])
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.target = len(graph) - 1
        self.graph = graph
        self.sol = []
        self.dfs([0])
        return self.sol