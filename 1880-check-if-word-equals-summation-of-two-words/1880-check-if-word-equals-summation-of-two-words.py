class Solution:
    def toStr(self, word):
        sol = ""
        for i in word:
            sol += str(ord(i) - ord("a"))
        return sol
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a,b,c = self.toStr(firstWord).lstrip("0"), self.toStr(secondWord).lstrip("0"), self.toStr(targetWord).lstrip("0")
        # print(a, )
        if a == "":
            a = "0"
        if b == "":
            b = "0"
        if c == "":
            c = "0"
        if int(c) == int(a) + int(b):
            return True
        return False