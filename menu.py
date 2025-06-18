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


def main():

    menu_items = get_menu_dictionary("file.txt")
    total_price = 0

    while True: 
        order = input("Enter an item to order: ")
        exit = order.lower()
        if exit == "end":
            break
        try: 
            item_price = menu_items[order.title()]
        
        except:
            continue
        
       
        total_price = item_price + total_price
        print(f"Total: {total_price}")

        



main()