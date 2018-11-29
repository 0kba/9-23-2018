import datetime
class Product:
    def __init__(self, ProductId, ProductName, Category, Price):
        self.ProductId = ProductId
        self.ProductName = ProductName
        self.Category = Category
        self.Price = Price

    def __repr__(self):
        return (f"{self.ProductId} {self.ProductName} {self.Category} {self.Price}")


class Order:
    def __init__(self, OrderId, OrderDate, Quantity, ProductId):
        self.OrderId = OrderId
        self.OrderDate = self.__parse_date__(OrderDate)
        self.Quantity = Quantity
        self.ProductId = ProductId

    def __parse_date__(self,OrderDate):
        token = OrderDate.split("-")
        return datetime.date(int(token[0]), int(token[1]), int(token[2]))

    def __repr__(self):
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


def parsing_to_dictionary(file_name):
    file = read_contents_to_list(file_name)
    orders_dictionary = {}
    for line in file:
        items = line.split(",")
        if items[3] not in orders_dictionary:
          orders_dictionary[items[3]] = [Order(items[0],items[1],items[2],items[3])]
        else:
            orders_dictionary[items[3]].append([Order(items[0],items[1],items[2],items[3])])
    return orders_dictionary








def list_orders_using_ProudctId(dictionary,ProductId):
    for key in dictionary:
        if key == ProductId:
            return dictionary[key]

def search_by_name(products_list,searching_name):
    for product in products_list:
        if searching_name in product:
            return product





print(parsing_to_list("product.txt"))
print(parsing_to_dictionary("order.txt"))


