import bisect 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            print(stones)
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                temp = stones.pop()
                temp -= stones.pop()
                bisect.insort(stones, temp)
        try:
            return stones[-1]
        except:
            return 0