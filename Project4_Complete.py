# MSIT 501 - Project 4
#
# Initial code developed by: Frank J. Mitropoulos
#
# Final code implemented by: Rene Tejon


import pickle  # pickle makes it SO easy to load/save data from/to disk.


class Item:
    '''
        This class models an Item in a collection.
        An item has a category, description, value and quantity.
        For example: Antique, Desk, 250.00, 1
    '''

    def __init__(self, category, desc, value, quant):
        '''
           This is the constructor for the Item class. It creates an Item object
           from the parameters passed in by the user.
           Note that self must be used in order to refer to the object's properties

           This constructor should NOT need any modifications
        '''
        self.category = category
        self.desc = desc
        self.value = value
        self.quant = quant

    def display(self):
        '''
            This method simply displays the item properties in a nicely formatted manner.

            This method should NOT need any modifications.
        '''
        print("{:<30}{:<18}{:<13.2f}{:<7d}".format(self.desc, self.category, self.value, self.quant))


class Collection:
    '''
        The Collection class models a collection of Item objects.
        It also provides the methods necessary to display information related to this collection.
    '''

    def __init__(self):
        '''
            This is the constructor for the Collection class. Note that it initializes 
            a list. This list will contain Item objects.

            This constructor should NOT need any modifications.
        '''
        self.items = []

    def addItem(self, category, desc, value, quant):
        '''
        This method accepts information about the Item object to create in the parameter list.
        An Item object is created and then added to the list. 

        YOU MUST IMPLEMENT THIS METHOD
        '''
        item = Item(category.title(), desc.title(), value, quant)
        self.items.append(item)

    def displayAllItems(self):
        '''
        This method displays all the Item objects in a nicely formatted table.

        YOU MUST IMPLEMENT THIS METHOD
        '''
        print('\nCollection')
        print('=' * 70)
        print(f"{'Description':<30}{'Category':<18}{'Value':<13}{'Quantity':<10}")
        print('-' * 70)
        for item in self.items:
            Item.display(item)

    def displayAllCategories(self):
        '''
        This method displays all the categories in the collection in a nicely 
        formatted table. Note that each category is displayed exactly once.

        YOU MUST IMPLEMENT THIS METHOD
        '''
        print(f"\n{'Categories Available':<18}")
        print('=' * 70)
        print(f"{'Category':<18}")
        print('-' * 70)
        my_category = []
        item = [item.category for item in self.items]
        for i in item:
            if i not in my_category:
                print(f"{i:<18}")
            my_category.append(i)

    def displayAllItemsForCategory(self, category):
        '''
        This method displays all the item objects that are in the category specified in
        the parameter list. This should be displayed in a nicely formatted table.

        If no items exist for the given category then a message should be displayed to
        the user stating so.

        YOU MUST IMPLEMENT THIS METHOD 
        '''
        item_list = [item.category for item in self.items]
        if category.title() in item_list:
            print(f"\n{'Items for Category: ' + category.title():<18}")
            print('=' * 70)
            print(f"{'Description':<30}{'Category':<18}{'Value':<13}{'Quantity':<10}")
            print('-' * 70)
            for items in self.items:
                if category.title() == items.category:
                    Item.display(items)
        else:
            print('\nSorry that category does not exist.')

    def displayItemsOverValue(self, value):
        '''
        This method displays all item objects whose value is greater than or equal to the
        value specified in the parameter list.

        These items should be displayed in a nicely formatted table.

        YOU MUST IMPLEMENT THIS METHOD
        '''
        item_list = [item.value for item in self.items]
        for i in item_list:
            if i > value:
                break
        else:
            print(f"\n{'Sorry no value greater than $'}{value:<,.2f}{' found.'}")
            return

        print(f"\n{'Items with value above: $'}{value:<18,.2f}")
        print('=' * 70)
        print(f"{'Description':<30}{'Category':<18}{'Value':<13}{'Quantity':<10}")
        print('-' * 70)
        for item in self.items:
            if item.value > value:
                Item.display(item)

    def displayItemFromDescription(self, desc):
        '''
        This method displays the first occurrence of any item object whose description is
        the same as the description specified in the parameter list.

        This item should be displayed in a nicely formatted manner.

        If no item exists with the given description, then a message should be displayed
        stating so.

        YOU MUST IMPLEMENT THIS METHOD
        '''
        item_list = [item.desc for item in self.items]
        if desc.title() in item_list:
            print(f"\n{'Items from Description':<18}")
            print('=' * 70)
            print(f"{'Description':<30}{'Category':<18}{'Value':<13}{'Quantity':<10}")
            print('-' * 70)
            for items in self.items:
                if desc.title() == items.desc:
                    Item.display(items)
                    return
        else:
            print('\nSorry, no item exists with the given description.')

    def displayCollectionValue(self):
        '''
        This method should display the total value of the collection.
        The total value of each item is the item's value * the item's quantity.

        YOU MUST IMPLEMENT THIS METHOD 
        '''
        collection_value = 0
        total_value = [(item.value * item.quant) for item in self.items]
        for item in total_value:
            collection_value += item
        print(f"\n{'Total Value of Collection'}")
        print('=' * 70)
        print("${:<,.2f}".format(collection_value))


# This simple print menu function displays the menu.
# You should NOT need to modify this function.

def printMenu():
    print("")
    print("1. Display all items in my collection")
    print("2. Display all categories of my items")
    print("3. Display all items in a given category")
    print("4. Search for an item by description")
    print("5. Add an new item to my collection")
    print("6. Display all items above a given value")
    print("7. Calculate the total value of my collection")
    print("S. Save to disk")
    print("L. Load data from disk")
    print("Q. Quit")
    print()


# This is the main function that drives the program
# This function will be called when you run the program
# You should NOT need to modify this main function.
#
# This function is already implemented to display the menu,
# get input from the user and call the appropriate Collection class methods

def main():
    stuff = Collection()
    print()
    print('Welcome to my Collection Manager')
    while True:
        printMenu()
        selection = input("Please enter a selection: ").strip().upper()
        if selection not in ['1', '2', '3', '4', '5', '6', '7', 'S', 'L', 'Q']:
            print("Please enter a valid choice...")
            continue
        if selection == '1':
            stuff.displayAllItems()
        elif selection == '2':
            stuff.displayAllCategories()
        elif selection == '3':
            category = input("Enter category: ").strip()
            stuff.displayAllItemsForCategory(category)
        elif selection == '4':
            itemToFind = input("Enter item's description: ").strip()
            stuff.displayItemFromDescription(itemToFind)
        elif selection == '5':
            cat = input("Enter the item's category: ").strip()
            desc = input("Enter the item's description: ").strip()
            value = eval(input("Enter the item's value: "))
            quant = eval(input("Enter the item's quantity: "))
            stuff.addItem(cat, desc, value, quant)
            print("Item added")
        elif selection == '6':
            value = eval(input("Enter the value: "))
            stuff.displayItemsOverValue(value)
        elif selection == '7':
            stuff.displayCollectionValue()
        elif selection == 'S':
            pickle.dump(stuff, open("stuff.p", "wb"))
            print("Data saved...")
        elif selection == 'L':
            stuff = pickle.load(open("stuff.p", "rb"))
            print("Data loaded...")
        else:
            print("Thanks for using my Collection Manager")
            break


# This line of code runs the main function above automatically when you run the program.
if __name__ == "__main__":
    main()
