def stock_items():
    """
    Reading the text file and adding the elements in 2D list.
    """
    table = []

    stock = open("stock.txt", 'r')
    lines = stock.readlines()
    for line in lines: 
        elements = line.strip().split(", ")
        table.append(elements)

    stock.close()
    return table

def update_equipment_file(table):
    file = open("stock.txt" , "w")
    for item in table:
        file.write(", ".join(item) + "\n")
    file.close()


def display_stock():
    stock = open("stock.txt", 'r')
    lines = stock.readlines()

    print("-" * 81)
    print("|S.N |    \tITEM\t         |      BRAND\t    |    PRICE\t |    QUANTITY  |")
    print("-" * 81)

    item_number = 1
    for line in lines:
            data = line.strip().split(", ")  # Split the line into data elements
            item, brand, price, quantity = data  # Unpack the data elements
            print(f"| {item_number:2} | {item:25} | {brand:16} | {price:10} | {quantity:12} |")
            item_number += 1

    print("-" * 81)

    stock.close()

