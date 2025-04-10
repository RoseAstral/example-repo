class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
'''
A class defining the details of a shoe
    Attributes:
        County (Str) - the country the show is manufactured in.
        Code(Str) - the Code used to identify the shoe
        Product(Str) - The name of the shoe.
        Cost(Int) - The cost for a pair of the shoes
        Quantity(Int) - The amount shoes avalible in the inventory.
'''
    def get_cost(self):
        return self.cost
'''
        A method for returnig the cost of a shoe.
'''
    def get_quantity(self):
        return self.quantity
'''
        A method for returning the quantity of shoes avalible
'''
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
'''
        The string reference for each object
'''
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    import os
    a = "inventory.txt"
    if os.path.isfile(a):
        try:
            with open('inventory.txt', 'r') as file:
                next(file)
                for line in file:
                    data = line.strip().replace("/n",'')
                    country, code, product, cost, quantity = data.split(',')
                    oshoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(oshoe)
                    file.close
                print("The inventory has been read from the file")
        except:
            print('An Error has occured')
    else:
        print('The inventory file does not exist')
'''
This function takes the infomation stored in the inventory document and converts it to objects to be sotred in the shoe_list.
'''
def capture_shoes(country, code, product, cost, quantity):
    oshoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(oshoe)
    with open("inventory.txt", 'a') as file:
        file.writelines(f'\n{country},{code},{product},{cost},{quantity}')
        file.close
    print("The shoe has been added to the inventory")
'''
Parameters:
    County (Str) - the country the show is manufactured in.
    Code(Str) - the Code used to identify the shoe
    Product(Str) - The name of the shoe.
    Cost(Int) - The cost for a pair of the shoes
    Quantity(Int) - The amount shoes avalible in the inventory.
This function is used to add a new shoe both the text file and to the shoe_list.
'''
def view_all(shoes):
    from tabulate import tabulate
    data = []
    headers = ["country", "code", "product", "cost", "quantity"]
    for shoe in shoes:
        data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    table = tabulate(data, headers, tablefmt = "grid")
    print(table)
'''
Parameters:
    shoes - List
    The list of shoes to print
This functions prints to the terminal all the shoes and their infomation in a table formate.
'''
def re_stock(self):
    if len(self) == 0:
        print("Please read Inventory from text file")
    else:
        minlist = []
        for shoe in self:
            minlist.append(int(shoe.quantity))
        minquant = min(minlist)
        index = 0
        while(index < len(minlist)):
            if minlist[index] == minquant:
                break
            index +=1 
        minobject = shoe_list[index]
        print(f"The shoe in need of restock is {shoe_list[index]}")
        update = input("Please enter the amount of shoes you wish to restock: ")
        shoe_list[index] = Shoe(minobject.country,minobject.code,minobject.product,minobject.cost,update)
        with open("inventory.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate
            lines[index + 1] = f"{Shoe(minobject.country,minobject.code,minobject.product,minobject.cost,update)}\n"
            lines[0] = "Country,Code,Product,Cost,Quantity\n"
            file.writelines(lines)
            file.close
        print("The inventory has been updated")
'''
Parameters:
    self : list
        The list of shoes
This function searches the list for the shoe with the lowest quantity in stock and asks the user to update the quantity of that shoe and appends the data to both to the list and text file.
'''

def search_shoe(target, list):
    result = next((shoe for shoe in list if shoe.code == target), "This shoe is not in the inventory")
    print(result)
''' 
Parameters:
    Target : Str
        The code of the shoe to be searched
    List : list
        The lsit of shoes to be searched
This function searches for a specfic shoe object based on its code
'''
def value_per_item(list):
    for shoe in list:
        print(f'Code:{shoe.code} and Value: {int(shoe.cost) * int(shoe.quantity)}')
'''
Parameters:
    list : List 
        The list of shoes to have their value calculated
This function calculates the value for each shoe in the list.
'''
def highest_qty(list):
    if len(list) == 0:
        return None
    maxlist = []
    for shoe in list:
        maxlist.append(int(shoe.quantity))
    maxobject = max(maxlist)
    index = 0
    while(index < len(maxlist)):
        if maxlist[index] == maxobject:
            break
        index += 1
    print(f'The shoe with the highest quantity is {shoe_list[index]}.')
'''
Parameters:
    list : List
        The list of objects to searched
This function searches for the shoe that has the highest quantity avalible.
'''
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
selection = 0
while selection < 8:
    print("1 = read data from inventory text file")
    print('2 = capture shoe')
    print('3 = view the Inventory')
    print('4 = Item in need of restock')
    print('5 = Search for shoe by code')
    print('6 = see the value per item')
    print('7 = highest quantity item in inventory')
    selection = int(input('Please selection the number for the function you wish to preform:'))
    if selection == 1:
        shoe_list =[]
        read_shoes_data()
    elif selection == 2:
        if len(shoe_list) == 0:
            print("The shoe inventory has not been read from file")
        else:
            country = input('Please input country: ')
            code = input("Please enter code: ")
            product = input("please enter the product: ")
            cost = input("please enter the price of the item: ")
            quantity = input("Please enter the Quantity of the item: ")
            capture_shoes(country, code, product, cost, quantity)
    elif selection == 3:
        if len(shoe_list) == 0:
            print("The shoe inventory has not been read from file")
        else:
            view_all(shoe_list)
    elif selection == 4:
        re_stock(shoe_list)
    elif selection == 5:
        if len(shoe_list) == 0:
            print("The shoe inventory has not been read from file")
        else:
            code = input('Please enter the code for the shoe you are looking for:)
            search_shoe(code, shoe_list)
    elif selection == 6:
        if len(shoe_list) == 0:
            print("The shoe inventory has not been read from file")
        else:
            value_per_item(shoe_list)
    elif selection == 7:
        if len(shoe_list) == 0:
            print("The shoe inventory has not been read from file")
        else:
            highest_qty(shoe_list)
    else:
        print('Invalid selection')
