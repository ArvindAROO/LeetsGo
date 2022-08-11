class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(sorted([int(i) for i in nums])[-k])