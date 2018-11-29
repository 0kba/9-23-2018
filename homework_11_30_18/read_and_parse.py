class Product:
    def __init__(self, ProductId, ProductName, Category, Price):
        self.ProductId = ProductId
        self.ProductName = ProductName
        self.Category = Category
        self.Price = Price

    def print_whole (self):
        return (f"{self.ProductId} {self.ProductName} {self.Category} {self.Price}")


class Order:
    def __init__(self, OrderId, OrderDate, Quantity, ProductId):
        self.OrderId = OrderId
        self.OrderDate = OrderDate.__parse_date__(OrderDate)
        self.Quantity = Quantity
        self.ProductId = ProductId

    def __parse_date__(self,OrderDate):
        token = OrderDate.split("-")
        return int(token[1]) , int(token[2]) , int(token[0])

    def print_whole(self):
        return (f"{self.OrderId} {self.OrderDate} {self.Quantity} {self.ProductId}")




def open_file_and_skip_header(file_name):
    opened_file = open(file_name,"r")
    opened_file.readline()
    return opened_file

def read_contents_to_list(file_name):
    opened_file = open_file_and_skip_header(file_name)
    file_contents= opened_file.readlines()
    opened_file.close()
    return file_contents

def parsing_to_list(file_name):
    file = read_contents_to_list(file_name)
    products_list = []

    for line in file:
        items = line.split(",")
        products_list.append(Product(items[0],items[1],items[2],items[3]))
    return products_list

def parsing_to_dic(file_name):
    file = read_contents_to_list(file_name)
    orders_dictionary = {1:0,2:0,3:0}
    for line in file:
        items = line.split(",")
        orders_dictionary.append(Order(items[0],items[1],items[2],items[3]))


print(read_contents_to_list("product.txt"))
print(read_contents_to_list("order.txt"))
