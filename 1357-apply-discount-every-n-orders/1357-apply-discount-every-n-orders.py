class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = 100 - discount
        self.products = products
        self.prices = prices
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for i in range(len(product)):
            total += self.prices[self.products.index(product[i])] * amount[i]
        self.count += 1
        if self.count % self.n == 0:
            total *= (self.discount/100)
        return float(total)


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)