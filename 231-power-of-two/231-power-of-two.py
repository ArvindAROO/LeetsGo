class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        flag = 1
        while n ^ flag != 0:
            if flag > n:
                return False
            flag = flag << 1
        return True