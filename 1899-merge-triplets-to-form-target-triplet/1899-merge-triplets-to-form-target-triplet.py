class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        works = set()
        for t in triplets:
            if any(t[i] > target[i] for i in {0,1,2}):
                continue
            for i, v in enumerate(t):
                if target[i] == v:
                    works.add(i)
        return len(works) == 3

