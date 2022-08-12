class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        l = len(matrix)
        for i in matrix:
            if len(set(i)) != l:
                return False
        for i in range(l):
            s = set()
            for j in range(l):
                if (t:=matrix[j][i]) not in s:
                    s.add(t)
                else:
                    print(t)
                    return False
        return True