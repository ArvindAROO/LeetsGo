class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            # for i in range(n):
            res = self.countAndSay(n - 1)
            sol = ""
            res = list(res)
            while res != []:
                count = 1
                first = res.pop(0)
                while res != []:
                    if res[0] == first:
                        res.pop(0)
                        count += 1
                    else:
                        break
                sol += str(count) + str(first)

            return sol