class Solution:
    def __init__(self):
        self.maps = {}
    @lru_cache(None)
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode()]
        if n in self.maps:
            return self.maps[n]
        ans = []
        for i in range(1, n-1, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n-1-i):
                    ans.append(TreeNode(left=left, right=right))
        self.maps[n] = ans
        return ans