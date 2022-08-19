# from sortedcollections import SortedList
from bisect import insort
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = [sum([int(i) for i in str(k)]) for k in nums]
        # print(sums)
        maps = {}
        for index, val in enumerate(sums):
            if val in maps:
                insort(maps[val], nums[index])
            else:
                maps[val] = [nums[index]]
        # print(maps)
        del nums
        del sums
        maps = {key:val[-2:] for key, val in maps.items() if len(val) > 1}
        # print(maps)
        try:
            return max([val[-1] + val[-2] for val in maps.values()])
        except:
            return -1
        