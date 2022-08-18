class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sol = []
        maps = {}
        for index, val in enumerate(groupSizes):
            # print(index, val)
            if val in maps:
                maps[val].append(index)
            else:
                maps[val] = [index]
        # print(maps)
        
        for key, val in maps.items():
            for i in range(0, len(val), key):
                sol.append(val[i : i+key])
        return sol