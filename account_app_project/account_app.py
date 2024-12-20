import sys
import datetime
import os
from account_app_exceptions import *

'''
My first project after learning the basics of python.
Created it myself. Can you believe it took 825 lines of
code (minors the comments). Oh my God! That's so crazy, isn't it?

Test it out and see what I've made 😁.

Special note: if you come across any bug, just know I really
tried 😩.
'''


class AccountApp:

    '''
    When this AccountApp class gets instatiated, three empty
    Dictionaries are created. 

    What this essentially means is that
    we will be working with three temporary database.

    Ones created when you run this code.
    '''
    # constructor

    def __init__(self):

        self.date = {}
        self.items = {}
        self.items_sold_date = {}

        self.prompt()

    '''
    This method prompts the user to enter a command to perform
    a specific task. When a command is entered, the method
    assigned to that command is called.
    
    For instance, when the '_a' command is entered the
    self.add_item() method is called.
    '''
    # method

    def prompt(self):

        user_input = input(
            "\nStarting account, enter:\n_a - add item\n_u - update item\n_s - sell item\n_vs - view all sold items for a specific date\n_vt - view all sold items in text file\n_it - item info\n_vall - view all items in stock\n_itn - view all items in stock by name\n_d - delete item\n_q - quit\nHint - enter '_r' in any input field to return to this menu\n\n")

        match user_input:
            case '_a':
                print("\n-------- ADD ITEM --------")
                self.add_item()
            case '_u':
                self.update_item()
            case '_s':
                print("\n-------- SELL ITEM --------")
                self.sell_item()
            case '_vs':
                print("\n-------- VIEW ALL SOLD ITEMS FOR SPECIFIED DATE --------")
                self.get_sold_items_for_spec_date()
            case '_vt':
                self.print_all_sold_items()
                return self.prompt()
            case '_it':
                print("\n-------- VIEW ITEM INFO --------")
                self.get_item_info()
            case '_vall':
                self.get_all_items_in_stock()
            case '_itn':
                self.get_all_items_by_name()
                return self.prompt()
            case '_d':
                self.delete_item()
            case '_q':
                print('\nAre you sure you want to quit?')
                while True:
                    quit = input('\ny - yes\nn - no\n\n')
                    if quit.lower() not in ['y', 'n']:
                        continue
                    elif quit.lower() == 'n':
                        return self.prompt()
                    else:
                        sys.exit(
                            "\nYou Quit\n\nTHANKS FOR TRYING OUT KELVIN'S ACCOUNT APPLICATION 😉")
            case _:
                print("Invalid syntax")
                return self.prompt()

    '''
    This method checks for the '_r' command. When the '_r' command
    is entered in any input field, the self.prompt() method is called,
    meaning the user is taken back to the prompt section.
    '''
    # method

    def check_for_r_keyword(self, input):
        if input.lower() == '_r':
            self.prompt()
        else:
            return

    '''
    This method checks if the user has enter an empty input.
    '''
    # method

    def check_for_empty_input(self, d_input):
        try:
            if d_input == '':
                raise EmptyInputException("\nInput value cannot be empty")
        except Exception as error_message:
            print(error_message)
            d_input = input("\nEnter correct input:\n").title()
            return self.check_for_empty_input(d_input)
        else:
            return d_input

    '''
    This method checks if the value entered for quantity is
    actually a number value.  
    '''
    # method

    def check_qty(self, qty: str):

        enter_num_value = "\nEnter a number value"

        while True:
            if not qty.isdecimal():
                try:
                    raise QuantityException(enter_num_value)
                except Exception as error_message:
                    print(error_message)
                    qty = input("\nQuantity:\n")
            else:
                break

        return int(qty)

    '''
    This method checks if the value entered for price is
    actually a number value or decimal value with the point (2.34).  
    '''
    # method

    def check_price(self, price: str):

        enter_num_value = "\nEnter a number or decimal value"

        symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
                   '(', ')', '_', '-', '=', '+', '{', '}', '\\', '[', ']', '|', '"', "'", ':', ';', '<', '>', ',', '?', '/']

        for symbol in symbols:
            while True:
                if symbol in price:
                    try:
                        raise PriceException(enter_num_value)
                    except Exception as error_message:
                        print(error_message)
                        price = input("\nPrice $:\n")
                else:
                    break

        while True:
            if price.isalpha():
                try:
                    raise PriceException(enter_num_value)
                except Exception as error_message:
                    print(error_message)
                    price = input("\nPrice $:\n")
            else:
                break

        return float(price)

    '''
    This method sets up the date, asking the user to enter date
    values (day, month and year) while checking if the date values
    are correct.
    '''
    # method

    def n_date(self):

        print("\nEnter date (dd/mm/yyyy)")
        enter_num_value = "\nEnter a number value"
        valid_month = ['1', '2', '3', '4', '5',
                       '6', '7', '8', '9', '10', '11', '12']

        while True:
            day = input("\nDay (dd):\n")
            day = self.check_for_empty_input(day)
            self.check_for_r_keyword(day)

            if not day.isdecimal():
                try:
                    raise DayValueException(enter_num_value)
                except Exception as error_message:
                    print(error_message)
                    continue
            elif len(day) < 1 or len(day) > 2:
                try:
                    raise DayValueException(
                        "\nDay value should not be less than 1 or more than 2")
                except Exception as error_message:
                    print(error_message)
                    continue
            elif int(day) not in range(1, 32):
                try:
                    raise DayValueException(
                        "\nDay value should be from 1 - 31")
                except Exception as error_message:
                    print(error_message)
                    continue
            else:
                break

        day = int(day)

        while True:
            month = input("\nMonth (mm):\n")
            month = self.check_for_empty_input(month)
            self.check_for_r_keyword(month)

            if not month.isdecimal():
                try:
                    raise MonthValueException(enter_num_value)
                except Exception as error_message:
                    print(enter_num_value)
                    continue
            elif month not in valid_month:
                try:
                    raise MonthValueException(
                        "\nMonth value should be from 1 - 12")
                except Exception as error_message:
                    print(error_message)
                    continue
            else:
                break

        month = int(month)

        while True:
            year = input("\nYear (yyyy):\n")
            year = self.check_for_empty_input(year)
            self.check_for_r_keyword(year)

            if not year.isdecimal():
                try:
                    raise YearValueException(enter_num_value)
                except Exception as error_message:
                    print(enter_num_value)
                    continue
            elif len(year) < 4 or len(year) > 4:
                try:
                    raise YearValueException(
                        "\nYear value should not be less than or more than 4")
                except Exception as error_message:
                    print(error_message)
                    continue
            else:
                break

        year = int(year)

        org_date = datetime.date(year, month, day)
        f_date = org_date.isoformat()
        # Reversing the date string value.
        f_date = f_date.split('-')
        f_date.reverse()
        f_date = '-'.join(f_date)
        return f_date

    '''
    This method adds items to the self.item and self.date dictionaries: 
    two of our temporary datebase.
    '''
    # method

    def add_item(self):

        date = self.n_date()

        item_name = input("\nItem name:\n").title()
        item_name = self.check_for_empty_input(item_name)

        self.check_for_r_keyword(item_name)

        # Checks if the item to be added already exists.
        def check_item(item):

            while True:
                if item in self.items.keys():
                    try:
                        raise ItemException(f"\n{item} already in stock")
                    except Exception as error_message:
                        print(error_message)
                        item = input("\nItem name:\n").title()
                        item = self.check_for_empty_input(item)
                        self.check_for_r_keyword(item)
                else:
                    return item

        item_name = check_item(item_name)

        batch_no = input("\nBatch no:\n")
        batch_no = self.check_for_empty_input(batch_no)

        self.check_for_r_keyword(batch_no)

        qty = input("\nQuantity:\n")
        qty = self.check_for_empty_input(qty)

        self.check_for_r_keyword(qty)

        qty = self.check_qty(qty)

        # Checks if item quantity is zero.
        def zero_check(qty):
            while True:
                if qty <= 0:
                    try:
                        raise QuantityException('\nQuantity cannot be zero')
                    except Exception as error_message:
                        print(error_message)

                        qty = input('\nQuantity:\n')
                        self.check_for_r_keyword(qty)
                        qty = self.check_qty(qty)
                else:
                    return qty

        qty = zero_check(qty)

        price = input("\nPrice $:\n")
        price = self.check_for_empty_input(price)

        self.check_for_r_keyword(price)

        price = self.check_price(price)

        self.items.update({item_name: {

            'Item name': item_name,
            'Batch no': batch_no,
            'Quantity': qty,
            'Price': price
        }})

        if self.date == {}:
            self.date = {date: [self.items[item_name]]}
        elif date in self.date.keys():
            self.date[date].append(self.items[item_name])
        else:
            self.date[date] = [self.items[item_name]]

        # Goes into the value (which is a list) of the date key in the
        # self.date dictionary, and prints the last item.
        def item_added(tdate: list):

            print(f"\nItem added\n\nItem name - {tdate[-1]['Item name']}\nBatch no - {
                tdate[-1]['Batch no']}\nQuantity - {tdate[-1]['Quantity']}\nPrice - ${tdate[-1]['Price']:.2f}")

        item_added(self.date[date])

        while True:

            print("\nAdd more items for the specified date")

            add_more = input('\ny - yes\nn - no\n\n')

            if add_more.lower() == 'y':

                item_name = input("\nItem name:\n").title()
                item_name = self.check_for_empty_input(item_name)

                self.check_for_r_keyword(item_name)

                item_name = check_item(item_name)

                batch_no = input("\nBatch no:\n")
                batch_no = self.check_for_empty_input(batch_no)

                self.check_for_r_keyword(batch_no)

                qty = input("\nQuantity:\n")
                qty = self.check_for_empty_input(qty)

                self.check_for_r_keyword(qty)

                qty = self.check_qty(qty)

                qty = zero_check(qty)

                price = input("\nPrice $:\n")
                price = self.check_for_empty_input(price)

                self.check_for_r_keyword(price)

                price = self.check_price(price)

                self.items.update({item_name: {

                    'Item name': item_name,
                    'Batch no': batch_no,
                    'Quantity': qty,
                    'Price': price
                }})

                self.date[date].append(self.items[item_name])

                item_added(self.date[date])
            elif add_more.lower() == 'n':
                break
            else:
                continue

        self.prompt()

    '''
    This method sells items and saves them in the self.items_sold_date
    dictionary: our last temporary database
    '''
    # method

    def sell_item(self):

        items_being_sold = {}

        total_price = 0

        display_sold_items = []

        date = self.n_date()

        item_name = input('\nItem name:\n').title()
        item_name = self.check_for_empty_input(item_name)

        self.check_for_r_keyword(item_name)

        # Checks if the item to be sold doesn't exist.
        def check_sold_item(item):

            while True:
                if item not in self.items.keys():
                    try:
                        raise ItemException(
                            f"\n{item} not in stock for you to sell")
                    except Exception as error_message:
                        print(error_message)
                        item = input('\nItem name:\n').title()
                        item = self.check_for_empty_input(item)
                        self.check_for_r_keyword(item)
                else:
                    break

            return item

        item_name = check_sold_item(item_name)

        qty = input('\nQuantity:\n')
        qty = self.check_for_empty_input(qty)

        self.check_for_r_keyword(qty)

        qty = self.check_qty(qty)

        # Checks if the user wants to sell zero quantity
        # or more than the quantity of the item in the
        # database (our temporary database 😁)
        def check_qty_num(qty):

            while True:
                if qty > self.items[item_name]['Quantity']:
                    try:
                        raise QuantityException(f'\nQuantity is greater than the quantity of {
                            item_name} in stock')
                    except Exception as error_message:
                        print(error_message)

                        qty = input('\nQuantity:\n')
                        qty = self.check_for_empty_input(qty)
                        self.check_for_r_keyword(qty)
                        qty = self.check_qty(qty)
                elif qty <= 0:
                    try:
                        raise QuantityException('\nQuantity cannot be zero')
                    except Exception as error_message:
                        print(error_message)

                        qty = input('\nQuantity:\n')
                        qty = self.check_qty(qty)
                else:
                    return qty

        qty = check_qty_num(qty)

        price = self.items[item_name]['Price'] * qty

        total_price += price

        items_being_sold[item_name] = {

            'Item name': item_name,
            'Quantity': qty,
            'Price': price
        }

        display_sold_items = [items_being_sold[item_name]]

        if self.items_sold_date == {}:
            self.items_sold_date = {date: [items_being_sold[item_name]]}
        elif date in self.items_sold_date.keys():
            self.items_sold_date[date].append(items_being_sold[item_name])
        else:
            self.items_sold_date[date] = [items_being_sold[item_name]]

        while True:

            print('\nSell more?')

            sell_more = input('\ny - yes\nn - no\n\n')

            if sell_more.lower() == 'y':

                item_name = input('\nItem name:\n').title()
                item_name = self.check_for_empty_input(item_name)

                self.check_for_r_keyword(item_name)

                item_name = check_sold_item(item_name)

                qty = input('\nQuantity:\n')
                qty = self.check_for_empty_input(qty)

                self.check_for_r_keyword(qty)

                qty = self.check_qty(qty)

                qty = check_qty_num(qty)

                price = self.items[item_name]['Price'] * qty

                total_price += price

                items_being_sold.update({item_name: {

                    'Item name': item_name,
                    'Quantity': qty,
                    'Price': price
                }})

                display_sold_items.append(items_being_sold[item_name])

                self.items_sold_date[date].append(
                    items_being_sold[item_name])
            elif sell_more.lower() == 'n':

                print('\n--------- SOLD -----------')

                # This substracts all the items being sold quantity
                # from the actual items quantity in the database.
                for i in self.items.keys():
                    for j in items_being_sold.keys():
                        if i == j:
                            self.items[i]['Quantity'] = self.items[i].get(
                                'Quantity') - items_being_sold[j]['Quantity']

                qty0 = True

                # Thus, the remaining quantity of the items
                # that were just sold is zero, the items are
                # automatically deleted.
                while qty0:
                    for i in self.items.keys():
                        if self.items[i]['Quantity'] == 0:
                            del self.items[i]
                            break
                    else:
                        qty0 = False

                    continue

                # Immediately an item is deleted from the self.items
                # database, it is also deleted from the self.date
                # database.
                #
                # If the value of a date key in the self.date
                # dictionary becomes empty due to an item deleted,
                # the date key is also deleted.
                def empty_d():
                    empty_date = True

                    while empty_date:
                        for d in self.date.keys():
                            if self.date[d] == []:
                                del self.date[d]
                                break
                            else:
                                for item in self.date[d]:
                                    if item['Quantity'] == 0:
                                        del self.date[d][self.date[d].index(
                                            item)]
                                        return empty_d()

                        if [] in self.date.values():
                            continue
                        else:
                            empty_date = False

                empty_d()

                for item in display_sold_items:
                    print(f"\nItem name - {item['Item name']}\nQuantity - {
                        item['Quantity']}\nPrice - ${item['Price']:.2f}")

                print(
                    f"\n----------\nTotal Price - ${total_price:.2f}\n-----------")

                break
            else:
                continue

        self.prompt()

    '''
    This method allows the user to update the quantity
    and price of an item. 
    '''
    # method

    def update_item(self):

        print('\n-------- UPDATE ITEM ---------')

        while True:
            item_name = input("\nItem name:\n").title()
            item_name = self.check_for_empty_input(item_name)

            self.check_for_r_keyword(item_name)

            if item_name.lower() == '_n':
                self.get_all_items_by_name()
                return self.update_item()
            elif item_name not in self.items.keys():
                try:
                    raise ItemException(f"\n{
                        item_name} not in stock for you to update\nEnter '_n' to get all items name")
                except Exception as error_message:
                    print(error_message)
                    continue
            else:

                # Asks the user if they would update more items
                def more_item_update():
                    print("\nUpdate more items")

                    while True:
                        more_updates = input("\ny - yes\nn - no\n\n")
                        self.check_for_r_keyword(more_updates)

                        if more_updates.lower() not in ['y', 'n']:
                            continue
                        elif more_updates.lower() == 'y':
                            return self.update_item()
                        else:
                            self.prompt()

                print('\nEnter')
                while True:
                    what_to_update = input(
                        "\nq - to update Quantity\np - to update Price\n\n")

                    what_to_update = self.check_for_empty_input(what_to_update)

                    self.check_for_r_keyword(what_to_update)

                    if what_to_update.lower() == 'q':
                        qty = input(f"\nUpdate quantity for {item_name}:\n")

                        self.check_for_r_keyword(qty)

                        qty = self.check_qty(qty)

                        # Checks if the user has entered zero for the
                        # quantity of the updated item.
                        def zero_check(qty):
                            while True:
                                if qty <= 0:
                                    try:
                                        raise QuantityException(
                                            '\nQuantity cannot be zero')
                                    except Exception as error_message:
                                        print(error_message)

                                        qty = input(f"\nUpdate quantity for {
                                                    item_name}:\n")
                                        qty = self.check_for_empty_input(qty)

                                        self.check_for_r_keyword(qty)
                                        qty = self.check_qty(qty)
                                else:
                                    return qty

                        qty = zero_check(qty)

                        self.items[item_name]['Quantity'] = qty

                        print(f"\nThe Quantity for '{
                              item_name}' has been updated")

                        more_item_update()
                    elif what_to_update.lower() == 'p':
                        price = input(f"\nUpdate price for {item_name}:\n")
                        price = self.check_for_empty_input(price)

                        self.check_for_r_keyword(price)

                        price = self.check_price(price)

                        self.items[item_name]['Price'] = price

                        print(f"\nThe Price for {item_name} has been updated")

                        more_item_update()
                    else:
                        continue

    '''
    This method gets all the sold items for a specific date.
    
    It goes into the value (which is a list) of the date key 
    in the self.date dictionary and display all the 
    sold items to the user.
    '''
    # method

    def get_sold_items_for_spec_date(self):

        while True:
            date = input("\nEnter date (dd/mm/yy):\n")
            date = self.check_for_empty_input(date)

            self.check_for_r_keyword(date)

            if date == 'all_d':
                if self.items_sold_date == {}:
                    try:
                        raise DateException("\nNo date available")
                    except Exception as error_message:
                        print(error_message)
                        self.prompt()
                else:
                    print("\n------- ALL SOLD DATES --------\n")
                    for sdate in self.items_sold_date.keys():
                        print(sdate)
                    continue
            elif date not in self.items_sold_date.keys():
                try:
                    raise DateException(
                        "\nYou haven't sold any item for date entered\nEnter command 'all_d' to view all sold date")
                except Exception as error_message:
                    print(error_message)
                    continue
            else:
                print(f"\n----- All Sold Items For Date ({date}) -----")
                for item in self.items_sold_date[date]:
                    print(f"\nItem name - {item['Item name']}\nQuantity - {
                        item['Quantity']}\nPrice - ${item['Price']:.2f}")
                break

        self.prompt()

    '''
    This method prints all sold items to a text file
    '''
    # method

    def print_all_sold_items(self):

        with open("account_app_project/demo.txt", "a") as file:

            for d in self.items_sold_date.keys():

                file.write(f"Date sold ({d})\n\n")

                for item in self.items_sold_date[d]:
                    file.write(f"Item name - {item['Item name']}\nQuantity - {
                        item['Quantity']}\nPrice - ${item['Price']:.2f}\n\n")

        with open("account_app_project/demo.txt") as file:
            content = file.read()

        with open("account_app_project/all_sold_items.txt", "w") as file:
            file.write(content)

        if os.path.exists("account_app_project/demo.txt"):
            os.remove("account_app_project/demo.txt")

        print_success_msg = "\nAll sold items have been saved as a text file - check computer..."

        print(print_success_msg)

    '''
    This method gets the item name, batch number, quantity
    and price of a specific item, and display it to the user. 
    '''
    # method

    def get_item_info(self):

        while True:
            item = input('\nItem name:\n').title()
            item = self.check_for_empty_input(item)

            self.check_for_r_keyword(item)

            if item.lower() == '_n':
                self.get_all_items_by_name()
                print("\n-------- VIEW ITEM INFO --------")
                continue
            elif item not in self.items.keys():
                try:
                    raise ItemException(
                        f"\n{item} not in stock, or must have been auto deleted\ndue to quantity was 0\nEnter '_n' to get all items name")
                except Exception as error_message:
                    print(error_message)
                    continue
            else:
                print(f"\n--------- ITEM INFO ----------\n\nItem name - {self.items[item]['Item name']}\nBatch no - {
                      self.items[item]['Batch no']}\nQuantity - {self.items[item]['Quantity']}\nPrice - ${self.items[item]['Price']:.2f}")

                break

        self.prompt()

    '''
    This method gets all items in the self.date datebase with their
    dates included.
    '''
    # method

    def get_all_items_in_stock(self):

        if self.items == {}:
            try:
                raise ItemException(
                    "\nNo Item in Stock\nYou can start by adding some items...")
            except Exception as error_message:
                print(error_message)
                self.prompt()
        else:
            print('\n------- ALL ITEMS IN STOCK -------')

            for d in self.date.keys():

                print(f"\nDate added ({d})")

                for item in self.date[d]:
                    print(f"\nItem name - {item['Item name']}\nBatch no - {
                        item['Batch no']}\nQuantity - {item['Quantity']}\nPrice - ${item['Price']:.2f}")

        self.prompt()

    '''
    This method gets all items by their names and display 
    to the user.
    '''
    # method

    def get_all_items_by_name(self):

        try:
            if self.items == {}:
                raise ItemException('\nNo item to display')
        except Exception as error_message:
            print(error_message)
            self.prompt()
        else:
            print('\n----- ALL ITEMS IN STOCK BY NAME -----\n')
            for all_items_name in self.items.keys():
                print(all_items_name)

        return

    '''
    This method deletes an item from the self.date and self.items
    dictionaries.
    '''
    # method

    def delete_item(self):

        print('\n-------- DELETE ITEM ---------')

        while True:
            item = input("\nItem name:\n").title()
            item = self.check_for_empty_input(item)

            self.check_for_r_keyword(item)

            if item.lower() == '_n':
                self.get_all_items_by_name()
                return self.delete_item()
            elif item not in self.items.keys():
                try:
                    raise ItemException(
                        "\nCan't delete because item doesn't exist\nEnter '_n' to get all items name")
                except Exception as error_message:
                    print(error_message)
                    continue
            else:
                print(f"\nAre you sure you want to delete {item}?")

                while True:
                    delete_input = input('\ny - yes\nn - no\n\n')
                    delete_input = self.check_for_empty_input(delete_input)

                    self.check_for_r_keyword(delete_input)

                    if delete_input.lower() == 'y':

                        # Deletes an item from the self.date
                        # database
                        for d in self.date.keys():
                            for t in self.date[d]:
                                if t['Item name'] == item:
                                    del self.date[d][self.date[d].index(t)]

                        # If a date becomes empty after the item has
                        # been deleted from that date in the self.date
                        # dictionary, the date key gets deleted too.
                        while True:
                            for d in self.date.keys():
                                if self.date[d] == []:
                                    del self.date[d]
                                    break

                            if [] in self.date.values():
                                continue
                            else:
                                break

                        # The item is deleted from the self.items
                        # dictionary.
                        del self.items[item]

                        print(f"\n{item} has been deleted")

                        delete_more_items = True

                        print("\nDelete more items?")

                        while delete_more_items:
                            more_deletes = input("\ny - yes\nn - no\n\n")
                            self.check_for_r_keyword(more_deletes)

                            if more_deletes.lower() not in ['y', 'n']:
                                continue
                            elif more_deletes.lower() == 'y':
                                return self.delete_item()
                            else:
                                self.prompt()
                    elif delete_input.lower() == 'n':
                        self.prompt()
                    else:
                        continue

    '''
    This part is for reference. 😉
    '''
    # # method
    # def delete_added_date(self):

    #     print('\n-------- DELETE DATE ---------')

    #     while True:
    #         date = input("\nEnter date (dd/mm/yy):\n")
    #         date = self.check_for_empty_input(date)

    #         self.check_for_r_keyword(date)

    #         if date == 'all_d':
    #             if self.date == {}:
    #                 try:
    #                     raise DateException("\nNo date available")
    #                 except Exception as error_message:
    #                     print(error_message)
    #                     self.prompt()
    #             else:
    #                 print("\n------- ALL DATES --------\n")
    #                 for sdate in self.date.keys():
    #                     print(sdate)
    #                 continue
    #         elif date not in self.date.keys():
    #             try:
    #                 raise DateException(
    #                     "\nCan't delete date because date doesn't exist\nEnter command 'all_d' to view all added date")
    #             except Exception as error_message:
    #                 print(error_message)
    #                 continue
    #         else:
    #             if self.date[date] == []:
    #                 del self.date[date]
    #                 print("\nDate successfully deleted")

    #                 delete_more_dates = True

    #                 print("\nDelete more dates")

    #                 while delete_more_dates:
    #                     more_dates_delete = input("\ny - yes\nn - no\n\n")
    #                     self.check_for_r_keyword(more_dates_delete)

    #                     if more_dates_delete.lower() not in ['y', 'n']:
    #                         continue
    #                     elif more_dates_delete.lower() == 'y':
    #                         return self.delete_added_date()
    #                     else:
    #                         self.prompt()
    #             else:
    #                 try:
    #                     raise DateException(
    #                         "\nCan't delete date - there are items assigned to date")
    #                 except Exception as error_message:
    #                     print(error_message)
    #                     continue
