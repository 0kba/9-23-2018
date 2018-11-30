class Order:
    def __init__(self, OrderId, OrderDate, Quantity, ProductId):
        self.OrderId = OrderId
        self.OrderDate = self.__parse_date__(OrderDate)
        self.Quantity = Quantity
        self.ProductId = ProductId

    def __repr__(self):
        return (f"{self.OrderId} {self.OrderDate} {self.Quantity} {self.ProductId}")

    def __parse_date__(self,OrderDate):
        token = OrderDate.split("-")
        return datetime.datetime.strptime( f'{token[0]}-{token[1]}-{token[2]}','%Y-%m-%d').date()