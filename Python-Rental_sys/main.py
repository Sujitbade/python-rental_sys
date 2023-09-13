
import read
import operation

print("-" * 50)
print("-"*20, " Welcome", "-"*20)
print("-" * 50)


def main():
    while True:
        print("Please select one the following option:")
        print("1.Stock - View the stocks")
        print("2.Rent - Rent out item from the shop.")
        print("3.Return - Return the items to the shop.")
        print("4.Exit - Exit the system.")
        print("\n")
        user_input = input(
            "Choose of the option:Rent/Return/Exit/Stock :").upper()
        if (user_input == "RENT"):
            first_name = input("Enter first name of the customer").capitalize()
            while not first_name.isalpha():
                print("\nEnter a valid first name")
                first_name = input("\nEnter first name of the customer").capitalize()
            last_name = input("Enter last name of the customer").capitalize()
            while not last_name.isalpha():
                print("\nEnter a valid last name")
                last_name = input(
                    "\n Enter last name of the customer").capitalize()
            customer_name = first_name+"_"+last_name

            while True:
                try:
                    phone_number = int(
                        input("\nEnter the phone number of the customer :"))
                    validation_number = str(phone_number)

                    if len(validation_number) == 10:
                        break
                    elif len(validation_number) < 10:
                        print("The phone number cannot be less than 10 numbers \n")
                    elif len(validation_number) > 10:
                        print("The phone number cannot contain more than 10 numbers")
                except ValueError:
                    print("Please enter a valid number \n")

            operation.renting_item(customer_name, phone_number)

        elif (user_input == "RETURN"):
            first_name = input("Enter first name of the customer").capitalize()
            last_name = input("Enter last name of the customer").capitalize()
            while not first_name.isalpha():
                print("\n Enter a valid first name")
                first_name = input(
                    "\nEnter first name of the customer").capitalize()
            while not last_name.isalpha():
                print("\n Enter a valid last name")
                last_name = input(
                    "\n Enter last name of the customer").capitalize()
            customer_name = first_name+"_"+last_name

            while True:
                try:
                    phone_number = int(
                        input("Enter the phone number of the customer :"))
                    validation_number = str(phone_number)

                    if len(validation_number) == 10:
                        break
                    else:
                        print(
                            "\n The phone number cannot contain less than 10 numbers!!!")
                except ValueError:
                    print("Please enter a valid number \n")

            operation.returning_item(customer_name, phone_number)

        elif (user_input == "STOCK"):
            read.display_stock()
        elif (user_input == "EXIT"):
            print("Exiting........")
            break
        else:
            print("\nPlease choose a valid option\n")
main()
