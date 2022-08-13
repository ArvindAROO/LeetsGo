class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        # for i in range(2 ** k):
        #     if (t:=bin(i)[2:].zfill(k)) not in s:
        #         return False
        #     # print(t)
        # return True
        a = set(s[i:i + k] for i in range(len(s) - k + 1))
        # if len(a) == 2 ** k:
        #     return True
        # return False
        return a.__len__() == 2 << k - 1
        