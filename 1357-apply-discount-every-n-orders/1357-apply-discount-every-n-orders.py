class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n=n
        self.c=0
        self.d=discount
        self.p=products
        self.pr=prices
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.bill=0
        self.c+=1
        for i,j in zip(product,amount):
            self.bill=self.pr[self.p.index(i)]*j+self.bill
        if(self.c==self.n):
            self.bill=self.bill * ((100 - self.d) / 100)
            self.c=0
            return self.bill
        return self.bill

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)