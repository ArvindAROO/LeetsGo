class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            size = len(mat)*len(mat[0])
            if size != r *c:
                return mat
            sol = []
            for i in mat:
                sol.extend(i)
            res = []
            i = 0
            for j in range(r):
                res.append(sol[i:c+i])
                i += c
            return res
        except:
            return mat
                