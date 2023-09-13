import read
import invoice
import datetime


def renting_item(customer_name, phone_number):
    table = read.stock_items()
    read.display_stock()
    selected = []
    rent_amount = 0

    while True:
        print("\n")
        try:
            item_id = int(input("Enter the Item ID")) - 1         
            if item_id < 0 or item_id >= len(table):
                print("Enter a valid Item ID")
                continue
            item_selected = table[item_id]
            while True:
                try:
                    quantity = int(input("Enter the number of quantity to rent"))
                    if quantity <= 0:
                        print("Please enter a positive number")
                        continue
                    if quantity > int(item_selected[3]):
                        print("Insuffiecient quantity available for rent")
                    else:    
                        item_selected[3] = str(int(item_selected[3]) - quantity)
                        read.update_equipment_file(table)
                        rent_amount = int(item_selected[2][1:]) * quantity

                        # Assigning the equiment sold information to appropriate variables
                        item_name = table[item_id][0]
                        item_price = table[item_id][2]
                        amount = rent_amount
                        quantity_renting = quantity
                        selected.append(
                            [item_name, item_price, quantity_renting, amount])

                    # Asking if customer wants to add more items
                        add_loop = False
                        while not add_loop:
                            continue_adding = input(
                                "Do you want to add more items?(Yes/No) : ").capitalize()
                            if continue_adding == "Yes":
                                add_loop = True
                            elif continue_adding == "No":
                                current_time = datetime.datetime.now()
                                date = current_time.strftime("%y-%m-%d %H-%M")
                                invoice.renting_invoice(
                                    customer_name, phone_number, date, selected)
                                invoice.renting_bill(
                                    customer_name, phone_number, date, selected)
                                return
                            else:
                                print("Please enter 'Yes' or 'No'")
                        break
                except ValueError:
                    print("Invalid quantity. Please enter a valid number\n")
        except ValueError:
            print("Invalid Item ID. Please enter a valid number\n")

def returning_item(customer_name, phone_number):
    table = read.stock_items()
    # read.display_stock()
    returning = []
    return_amount = 0

    # Insert a try and catch
    while True:
        print("\n")
        try:
            item_id = int(input("Enter the Item ID of the item that the customer wishes to return :")) - 1
            if item_id < 0 or item_id > len(table):
                print("Enter a valid Item ID")
                continue

            item_selected = table[item_id]
            while True:
                try:
                    quantity = int(input("Enter the number of quantity to retrun"))
                    if quantity < 0:
                        print("Enter a positive quantity")
                        continue

                    return_days = int(input("Enter the number of days the item was rented :"))
                    if return_days <= 0:
                        print("The return day must be more than 0 days")
                        continue
                    if return_days <= 5:
                        item_selected[3] = str(int(item_selected[3]) + quantity)
                        read.update_equipment_file(table)
                        return_amount = int(item_selected[2][1:]) * quantity

                        # Assigning the equiment sold information to appropriate variables
                        item_name = table[item_id][0]
                        item_price = table[item_id][2]
                        amount = return_amount
                        quantity_returning = quantity
                        exceed_fine = 0
                        returning.append(
                            [item_name, item_price, quantity_returning, amount, exceed_fine])

                        # Asking if customer wants to add more items
                        add_loop = False
                        while not add_loop:
                            continue_adding = input(
                                "Do you want to return more items?(Yes/No) : ").capitalize()
                            if continue_adding == "Yes":
                                add_loop = True
                            elif continue_adding == "No":
                                current_time = datetime.datetime.now()
                                date = current_time.strftime("%y-%m-%d %H-%M")
                                invoice.returning_invoice(
                                    customer_name, phone_number, date, returning, return_days)
                                invoice.returning_bill(
                                    customer_name, phone_number, date, returning,return_days)
                                return
                            else:
                                print("Please enter 'Yes' or 'No'")
                        break
                    elif return_days > 5:
                        exceeded_days = return_days - 5
                        item_selected[3] = str(int(item_selected[3]) + quantity)
                        read.update_equipment_file(table)
                        return_amount += int(item_selected[2][1:]) * quantity
                        exceed_fine = int(item_selected[2][1:]) * exceeded_days * quantity

                        # Assigning the equiment sold information to appropriate variables
                        item_name = table[item_id][0]
                        item_price = table[item_id][2]
                        amount = return_amount
                        quantity_returning = quantity
                        returning.append(
                            [item_name, item_price, quantity_returning, amount, exceed_fine])

                        # Asking if customer wants to add more items
                        add_loop = False
                        while not add_loop:
                            continue_adding = input(
                                "Do you want to return more items?(Yes/No) : ").capitalize()
                            if continue_adding == "Yes":
                                add_loop = True
                            elif continue_adding == "No":
                                current_time = datetime.datetime.now()
                                date = current_time.strftime("%y-%m-%d %H-%M")
                                invoice.returning_invoice(
                                    customer_name, phone_number, date, returning, return_days)
                                invoice.returning_bill(
                                    customer_name, phone_number, date, returning,return_days)
                                return
                            else:
                                print("Please enter 'Yes' or 'No'")
                        break
                except ValueError:
                    print("Enter a valid quantity")
        except ValueError:
            print("Invalid item Item ID")
