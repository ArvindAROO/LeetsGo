import numpy as np
class Solution:
    def luckyNumbers (self, A: List[List[int]]) -> List[int]:
        A=np.array(A)
        return list(set(A.max(axis=0)).intersection(A.min(axis=1)))
        # minArray = set(min(i) for i in matrix)
        # maxArray = set()
        # for j in range(len(matrix)):
        #     for k in range(len(matrix[0])):
        #         temp = set()
        #     maxArray.add(max(i) for i in matrix[j][k])
        # print(minArray, maxArray)