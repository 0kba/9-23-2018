import datetime
import sys

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
        return datetime.datetime.strptime( f'{token[0]}-{token[1]}-{token[2]}','%Y-%m-%d').date()

    def __repr__(self):
        return (f"{self.OrderId} {self.OrderDate} {self.Quantity} {self.ProductId}")


def open_file_and_skip_header(file_name):
    opened_file = open(file_name,"r")
    opened_file.readline()
    return opened_file

def read_contents_to_list(file_name):
    opened_file = open_file_and_skip_header(file_name)
    file_contents= opened_file.read().splitlines()
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
        else:
            return "not found please try again"

def search_by_name(products_list,searching_name):
    for product in products_list:
        if searching_name.lower() == product.ProductName.lower():
            return product
        else:
            return "not found please try again"

def list_by_catagory(products_list):
    catagory_dictionary = {}
    for product in products_list:
        if product.Category not in catagory_dictionary:
            catagory_dictionary[product.Category] = [product]
        else:
            catagory_dictionary[product.Category].append([product])
    return catagory_dictionary

def combine_list_of_lists (main_list):
    result_list = []
    for item in main_list:
        if type(result_list) == type(item):
            peel_list_layer(result_list, item, main_list)
        else: result_list.append(item)
    return result_list

def peel_list_layer(result_list, item, main_list):
    for list in item:
        if type(result_list) == type(list):
            main_list.append(list)
        else:
            result_list.append(list)

def dictionary_values_to_list(orders_dictionary):
    values = []
    for key in orders_dictionary.keys():
        values.append(orders_dictionary[key])
    orders = combine_list_of_lists(values)
    return orders

def orders_between_2dates(orders_dictionary,date1,date2):
    result = []
    orders = dictionary_values_to_list(orders_dictionary)
    if date1 < date2:
        temp = date1
        date1 = date2
        date2 = temp
    for order in orders:
        if date2 <= order.OrderDate <= date1 :
            result.append(order)
    if result == []:
        return "no orders have been found please try again"
    return result

def import_2dates_from_user(orders_dictionary):
    print("please enter the first date in this format Y-M-D then press Enter")
    date1 = input(datetime.datetime)
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
    print("please enter the second date in this format Y-M-D then press Enter")
    date2 = input(datetime.datetime)
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
    return (orders_between_2dates(orders_dictionary, date1, date2))

def options_output (first_file,second_file,option):
    products_list = parsing_to_list(first_file)
    orders_dictionary = parsing_to_dictionary(second_file)
    if option == '1':
       return (list_by_catagory(products_list))
    elif option == '2':
        ProductId = input(print("please enter the ProductId"))
        return (list_orders_using_ProudctId(orders_dictionary, ProductId))
    elif option == '3':
        searching_name = input(print("please enter the name of the product you want to search for"))
        return (search_by_name(products_list, searching_name))
    elif option == '4':
        return import_2dates_from_user(orders_dictionary)

def __main__():
    if len(sys.argv) < 3:
        print("Please write two valid files names separated by space then you will get options")
        return
    try:
        first_file = sys.argv[1]
        second_file = sys.argv[2]
        option = None
        while option != '0':
            option = input(print(f"""please Enter: 
            0 - to quit
            1 - to list all products grouped by categories
            2 - to list all orders for a given product (your program should then ask for the product id) 
            3 - to search products by name 
            4 - to see orders between a specific date range."""""))
            if '4' >= option >= '1':
                print(options_output(first_file, second_file, option))
            elif option != '0':
                print("that isn't a valid entry please try again")
        if option == '0':
            print("bye bye")
            return

    except IndentationError:
        print(f"{sys.argv} is not a valid entry", file=sys.stderr)
        return
    except FileNotFoundError:
        print(f"one or both of your files doesn't exist", file=sys.stderr)
        return


__main__()
