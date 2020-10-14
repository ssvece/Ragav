# Program for inventory management

def menu(s):
    switcher = {
        1: add_item(),
        2: "Update Item",
        3: "Delete Item"
    }
    return switcher.get(s, "Invalid day of week")


def add_item():
    item_list=[]
    item_name = input("Enter the name of the Item : ")
    item_qty = input("Enter Quantity of the item : ")
    item_type = input("Enter the Type like routers, switch .etc : ")
    item_list.append[item_name, item_type, item_qty]


options = int(input("Enter 1 for Add item\n\t  2 for Update Item\n\t  3 for Delete Item  \n\t  : "))
menu(options)
#print(item_list)
#1add_item()

