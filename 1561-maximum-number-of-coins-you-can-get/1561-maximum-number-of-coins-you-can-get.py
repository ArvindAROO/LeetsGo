class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        return max([sum([piles[i] for i in range(1, len(piles), 3)]), sum(piles[len(piles) // 3 : 2 * len(piles) // 3]), sum([piles[i] for i in range(1, 2 * len(piles) // 3, 2)])])