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

    def __repr__(self):
        return (f"{self.OrderId} {self.OrderDate} {self.Quantity} {self.ProductId}")

    def __parse_date__(self,OrderDate):
        token = OrderDate.split("-")
        return datetime.datetime.strptime( f'{token[0]}-{token[1]}-{token[2]}','%Y-%m-%d').date()

def open_file_and_skip_header(file_name):
    opened_file = open(file_name,"r")
    opened_file.readline()
    return opened_file

def read_contents(file_name):
    opened_file = open_file_and_skip_header(file_name)
    file_contents= opened_file.read().splitlines()
    opened_file.close()
    return file_contents

def parsing_to_list(products_file):                               # saving items for the products file
    file = read_contents(products_file)                   # in a list by parsing it with the class
    products_list = []
    for line in file:
        items = line.split(",")
        products_list.append(Product(items[0],items[1],items[2],items[3]))
    return products_list

def parsing_to_dictionary(orders_file):                         # saving items for the orders file in a dictionary
    file = read_contents(orders_file)                   # by parsing it with a class using ProductId as a key
    orders_dictionary = {}
    for line in file:
        items = line.split(",")
        if items[3] not in orders_dictionary:
          orders_dictionary[items[3]] = [Order(items[0],items[1],items[2],items[3])]
        else:
            orders_dictionary[items[3]].append([Order(items[0],items[1],items[2],items[3])])    # saving all orders
    return orders_dictionary                                                           # related to product in one value

def list_by_catagory(products_list):                                      # option number one using dictionarry
    catagory_dictionary = {}
    for product in products_list:
        if product.Category not in catagory_dictionary:
            catagory_dictionary[product.Category] = [product]
        else:
            catagory_dictionary[product.Category].append([product])      # saving all products related to the same
    return catagory_dictionary                                           # catagory in one value

def list_orders_by_ProudctId(orders_dictionary, ProductId):                   # option number two
    for key in orders_dictionary:
        if key == ProductId:                                             # using the key we saved before in
            return orders_dictionary[key]                                       # parsing_to_dictionary function
    else:
        return "not found please try again"

def search_by_name(products_list,searching_name):                        # option number three
    for product in products_list:
        if searching_name.lower() == product.ProductName.lower():
            return product
    else:
        return "not found please try again"

# next 3 functions to handle option 4 (search orders between two dates)
def parsing_orders_to_list(orders_file):                        # saving all orders in on list
    file = read_contents(orders_file)
    orders_list = []
    for line in file:
        items = line.split(",")
        orders_list.append(Order(items[0],items[1],items[2],items[3])) # parsing it with a class so we can compare it
    return orders_list

def import_2dates_from_user(orders_file):                      # taking the two dates from the user
    try:
        print("please enter the first date in this format Y-M-D then press Enter")
        date1 = input(datetime.datetime)
        date1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()      # in the same manner we saved
        print("please enter the second date in this format Y-M-D then press Enter")  #  the dates in the file
        date2 = input(datetime.datetime)
        date2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
        return (search_orders_between_2dates(orders_file, date1, date2))
    except ValueError:
        print("one or both of your dates not valid please try again",file=sys.stderr)

def search_orders_between_2dates(orders_file, date1, date2):         # searching and comparing the dates
    result = []
    orders = parsing_orders_to_list(orders_file)
    if date1 < date2:
        temp = date1                                                 # just in case user entered the older date first
        date1 = date2
        date2 = temp
    for order in orders:
        if date2 <= order.OrderDate <= date1 :
            result.append(order)
    if result == []:
        return "no orders have been found please try again"
    return result
# that was the last function to handle option number 4

def options_output (products_file, orders_file, option):    # this function to handle all valid option inputs except quiting
    products_list = parsing_to_list(products_file)
    orders_dictionary = parsing_to_dictionary(orders_file)
    option_catagory = '1'
    option_productId = '2'
    option_name_search = '3'
    option_date_search = '4'
    if option == option_catagory:
       return (list_by_catagory(products_list))
    elif option == option_productId:
        ProductId = input(print("please enter the ProductId"))
        return (list_orders_by_ProudctId(orders_dictionary, ProductId))
    elif option == option_name_search:
        searching_name = input(print("please enter the name of the product you want to search for"))
        return (search_by_name(products_list, searching_name))
    elif option == option_date_search:
        return import_2dates_from_user(orders_file)

def empty_file_handling (products_file, orders_file):        # this one to inform the user from the begining that
    products_list = parsing_to_list(products_file)          # that he provided an empty file
    orders_dictionary = parsing_to_dictionary(orders_file)
    if products_list == [] or orders_dictionary == {}:
        return  True

def __main__():
    if len(sys.argv) != 3:
        print("""   Please write products file name then orders file name
separated by spaces then you will be asked for options""")
        return
    try:
        products_file = sys.argv[1]
        orders_file = sys.argv[2]
        if empty_file_handling (products_file,orders_file):
            print( "one or both of your files are empty 0 to quit")
        option = None
        while option != '0':
            option = input(print(f"""please Enter: 
            0 - to quit
            1 - to list all products grouped by categories
            2 - to list all orders for a given product Id 
            3 - to search products by name 
            4 - to see orders between a specific date range."""""))
            if '4' >= option >= '1':
                print(options_output(products_file, orders_file, option))
            elif option != '0':
                print("that isn't a valid entry please try again")
        if option == '0':
            print("the programme has been closed")
            return

    except FileNotFoundError:
        print(f"one or both of your files doesn't exist", file=sys.stderr)
        return


__main__()

