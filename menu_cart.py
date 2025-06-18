"""
Function to load meny item and price into a dictionary
Input: (string)file_path
Output: menu(dictionary)
"""
def get_menu_dictionary(file_name:str) -> dict:
    data_file = open(file_name, "r")

    
    #create an empty dictionary to store item: price entries 
    menu_items = {}

    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #split the data at the comma
        item_name_and_price = line_of_data.split(",")
        
        #get the menu item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #create an entry in the dictionary for the item and price 
        menu_items[item_name] = item_price

    data_file.close()
    return menu_items


def display_cart(cart:dict, menu_items:dict) -> None:
    total = 0
    #loop through the cart to print the output
    for item, quantity in cart.items():
        total = total + (quantity * menu_items[item])
        print(f"{quantity} {item} @ {menu_items[item]:.2f}: {quantity * menu_items[item]}")
    print(f"\nTotal: {total}")

def main():

    menu_items = get_menu_dictionary("file.txt")
    total_price = 0
    #create a cart dictionary
    item_cart ={}

    while True: 
        #prompts user for item
        order = input("Enter an item to order: ")

        #determine if we need to end the program    
        exit = order.lower()
        if exit == "end":
            break
    
        #validate that item is in menu_item dictionary
        if order.title() not in menu_items:
            print(f"\n ERROR: {order} not on the menu" )
            continue

        #prompt user for quantity
        try:
            quantity = int(input("Quantity: "))
        except:
            print("\n ERROR: Enter number for quantity")
            continue

       
       
        #add item to cart, if item in cart already, quantity
        #if not in car add item and quantity to cart
        if order not in item_cart:
            #create a new entry in the item_cart dictionary
            item_cart[order.title()] = quantity
        else: 
            #adds quantity to the value of the item's current quantity
            item_cart[order.title()] += quantity
        
        #display total by calling the display cart function
        display_cart (item_cart, menu_items)
        
    

        """
        2 Taco @3.00: 6.00
        3 Bowl @8.50: 25.50

        Total: 31.50
        """

        



main()