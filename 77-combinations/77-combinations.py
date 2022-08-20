from itertools import combinations

class Solution:
#     def recur(self, n):
#         for i in range(1, n + 1):
            
    def combine(self, n: int, k: int) -> List[List[int]]:
#         sol = [[]]
#         steps = 1

#         for i in range(steps, n + 1):
#             copy = sol
#             sol = []
#             for j in copy:
#                 print(copy)
#                 j.append(i)
#                 sol.append(j)
#             steps += 1
#         return sol
        return combinations(list(range(1, n + 1)), k)