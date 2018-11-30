class Product:
    def __init__(self, ProductId, ProductName, Category, Price):
        self.ProductId = ProductId
        self.ProductName = ProductName
        self.Category = Category
        self.Price = Price

    def __repr__(self):
        return (f"{self.ProductId} {self.ProductName} {self.Category} {self.Price}")