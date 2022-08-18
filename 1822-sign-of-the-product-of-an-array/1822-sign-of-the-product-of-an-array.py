class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        return 1 if len([i for i in nums if i < 0]) & 1 == 0 else -1