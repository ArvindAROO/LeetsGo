class Solution:
    def minPairSum(self, arr: List[int]) -> int:
        arr.sort()
        return max(arr[i] + arr[-i -1] for i in range(len(arr) // 2))