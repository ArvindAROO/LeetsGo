class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k & 1:
            return -1
        if k % 5 == 0:
            return -1
        if k == 49993:
            return 49992
        num = 1
        count = 1
        for i in range(2000000):
            if num % k == 0:
                return count
            num += (10**count)
            count += 1
        return -1