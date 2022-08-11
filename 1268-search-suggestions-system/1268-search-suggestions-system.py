class Solution:
    def init(self, letter):
        for i in self.products:
            if i[0] == letter:
                self.sol[0].append(i)
    def helper(self, letter, num):
        temp = self.sol[-1]
        self.sol.append([])
        for i in temp:
            try:
                if i[num] == letter:
                    self.sol[-1].append(i)
            except:
                pass
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.products = sorted(products)
        self.sol = [[]]
        self.init(searchWord[0])
        for i in range(1, len(searchWord)):
            self.helper(searchWord[i], i)
        res = []
        for i in self.sol:
            if len(i) > 3:
                res.append(i[:3])
            else:
                res.append(i)
        return res