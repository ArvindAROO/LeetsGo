class Solution:
    def check(self, word):
        j = 0
        for i in word:
            if j > self.l:
                return False
            else:
                try:
                    while self.s[j] != i:
                        j+= 1
                    else:
                        j+=1
                except:
                    return False
        return True
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        self.l = len(s)
        self.s = s
        maps = {}
        maps = {i:words.count(i) for i in set(words)}
        # self.s = maps
        for i in maps:
            if self.check(i):
                # print(i)
                count += maps[i]
                # print(maps[i])
        return count