from sortedcontainers import SortedList
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        temp = SortedList()
        total =0
        for i in nums:
            temp.add(i)
            total += i
        goal = total / 2
        c = 0
        while total > goal:
            largest = temp.pop()
            total -= largest / 2
            temp.add(largest / 2)
            c += 1
        return c