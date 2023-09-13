import operation


def renting_invoice(customer_name, phone_number, date, selected):
    total_amount = 0
    print("=" * 80)
    print("|                           EventPal Rentals                                   |")
    print("|                     Bhaktapur, Madhyapur Thimi-7                             |")
    print("|               Your Event, Our Expertise , Endless Options                    |")
    print("=" * 80)
    print("{}{:<67}{}".format("| Rent Date:", date, "|"))
    print("{:5}{:<48}{}{}{}".format(
        "| Name:", customer_name, "Phone Number :", phone_number, "|"))
    print("=" * 80)
    print("{:<35} {:<15} {:<15} {:<15} ".format(
        "| Description", "|Price(5days)", "|  Quantity", "|  Amount  |"))
    print("=" * 80)
    for lines in selected:
        print("{}{:<35}{}{:<15}{}{:<15}{}{:<10}{}".format(
            "|", lines[0], "|", lines[1], "|", lines[2], "|", lines[3], "|"))
        total_amount += lines[3]
    print("=" * 80)
    print("{:<52}{:<16}{}{:<10}{}".format(
        "|", "|Total Amount", "|", total_amount, "|"))
    print("=" * 80)


def renting_bill(customer_name, phone_number, date, selected):
    total_amount = 0
    invoice_name = customer_name + "_" + \
        date.replace(" ", "_") + str(phone_number) + ".txt"
    rent_bill = open(invoice_name, "w")
    rent_bill.write("=" * 80 + "\n")
    rent_bill.write(
        "|                           EventPal Rentals                                   |\n")
    rent_bill.write(
        "|                     Bhaktapur, Madhyapur Thimi-7                             |\n")
    rent_bill.write(
        "|               Your Event, Our Expertise , Endless Options                    |\n")
    rent_bill.write("=" * 80 + "\n")
    rent_bill.write("{}{:<67}{}\n".format("| Rent Date:", date, "|"))
    rent_bill.write("{:5}{:<48}{}{}{}\n".format(
        "| Name:", customer_name, "Phone Number :", phone_number, "|"))
    rent_bill.write("=" * 80 + "\n")
    rent_bill.write("{:<35} {:<15} {:<15} {:<15}\n".format(
        "| Description", "|  Price", "|  Quantity", "|  Amount  |"))
    rent_bill.write("=" * 80 + "\n")
    for lines in selected:
        rent_bill.write("{}{:<35}{}{:<15}{}{:<15}{}{:<10}{}\n".format(
            "|", lines[0], "|", lines[1], "|", lines[2], "|", lines[3], "|"))
        total_amount += lines[3]
    rent_bill.write("=" * 80 + "\n")
    rent_bill.write("{:<52}{:<16}{}{:<10}{}\n".format(
        "|", "|Total Amount", "|", total_amount, "|"))
    rent_bill.write("=" * 80)
    rent_bill.close()


def returning_invoice(customer_name, phone_number, date, returning,return_days):
    sub_total = 0
    fine = 0
    print("=" * 80)
    print("|                           EventPal Rentals                                   |")
    print("|                     Bhaktapur, Madhyapur Thimi-7                             |")
    print("|               Your Event, Our Expertise , Endless Options                    |")
    print("=" * 80)
    print("{}{:<45}{}{:<6}{}".format("| Return Date:", date,"Rented days : ", return_days ,"|"))
    print("{:5}{:<48}{}{}{}".format(
        "| Name:", customer_name, "Phone Number :", phone_number, "|"))
    print("=" * 80)
    print("{:<35} {:<15} {:<15} {:<15} ".format(
        "| Description", "|  Price", "|  Quantity", "|  Amount  |"))
    print("=" * 80)
    for lines in returning:
        print("{}{:<35}{}{:<15}{}{:<15}{}{:<10}{}".format(
            "|", lines[0], "|", lines[1], "|", lines[2], "|", lines[3], "|"))
        fine += lines[4]
        sub_total += lines[3]

    total_amount = fine + sub_total

    print("=" * 80)
    print("{:<45}{:<23}{}{:<10}{}".format(
        "|", "|Sub Amount", "|", sub_total, "|"))
    print("{:<45}{:<16}{}{:<10}{}".format(
        "|", "|Fine(days exceeding 5)", "|", fine, "|"))
    print("{:<45}{:<23}{}{:<10}{}".format(
        "|", "|Total Amount", "|", total_amount, "|"))
    print("=" * 80)


def returning_bill(customer_name, phone_number, date, returning, return_days):
    sub_total = 0
    fine = 0
    invoice_name = customer_name+"_" + \
        date.replace(" ", "_")+str(phone_number)+".txt"
    return_bill = open(invoice_name, "w")
    return_bill.write("=" * 80 + "\n")
    return_bill.write("|                           EventPal Rentals                                   |\n")
    return_bill.write("|                     Bhaktapur, Madhyapur Thimi-7                             |\n")
    return_bill.write("|               Your Event, Our Expertise , Endless Options                    |\n")
    return_bill.write("=" * 80 + "\n")
    return_bill.write("{}{:<45}{}{:<6}{}\n".format("| Return Date:", date,"Rented Days : ",return_days, "|"))
    return_bill.write("{:5}{:<48}{}{}{}\n".format(
        "| Name:", customer_name, "Phone Number :", phone_number, "|"))
    return_bill.write("=" * 80 + "\n")
    return_bill.write("{:<35} {:<15} {:<15} {:<15}\n".format(
        "| Description", "|  Price", "|  Quantity", "|  Amount  |"))
    return_bill.write("=" * 80 + "\n")
    for lines in returning:
        return_bill.write("{}{:<35}{}{:<15}{}{:<15}{}{:<10}{}\n".format(
            "|", lines[0], "|", lines[1], "|", lines[2], "|", lines[3], "|"))
        fine += lines[4]
        sub_total += lines[3]

    total_amount = fine + sub_total

    return_bill.write("=" * 80+"\n")
    return_bill.write("{:<52}{:<16}{}{:<10}{}\n".format(
        "|", "|Sub Amount", "|", sub_total, "|"))
    return_bill.write("{:<52}{:<16}{}{:<10}{}\n".format(
        "|", "|Fine Amount", "|", fine, "|"))
    return_bill.write("{:<52}{:<16}{}{:<10}{}\n".format(
        "|", "|Total Amount", "|", total_amount, "|"))
    return_bill.write("=" * 80)
