def discount_calculate(amount):
    if amount >= 5000:
        return amount * 0.10
    elif amount >= 2000:
        return amount * 0.05
    else:
        return 0

def bill_add_fun():
    cutomer_name = input("Enter Customer Name: ")
    totalA_amount = 0
    while True:
        product_name = input("Enter Product Name: ")
        qty = int(input("Enter quantity: "))
        if qty < 0:
            print("Please enter positive value.")
        unit_price = float(input("Enter Product Unit price: "))
        if unit_price < 0:
            print("Please enter positive value.")

        product_price = qty * unit_price
        totalA_amount += product_price
        more = input("Do you want more (y/n)?")
        if more == 'y':
            continue
        else:
            break
    discount = discount_calculate(totalA_amount)
    net_payable_amount = totalA_amount - discount
    print("-----Bill Info---------")
    print(f'''
        Customer Name: {cutomer_name}
        Total Amount: {totalA_amount}
        Discount: {discount}
        Net Pay: {net_payable_amount}
    ''')

    with open('bill.txt', 'a') as file:
        file.write(f'Customer Name: {cutomer_name}, Total Amount: {totalA_amount}, Discount: {discount}, Net Pay: {net_payable_amount}\n')

def view_bill_fun():
    with open('bill.txt','r') as file:
        content = file.read()
        print(f'''
        ------------Bill History----------
        {content}
        ''')

while True:
    print('''
        1. Add Customer Bill
        2. View All Bills
        3. Exit
    ''')
    choice = input("Enter your choice: ")
    if choice == '1':
        bill_add_fun()
    elif choice == '2':
        view_bill_fun()
    elif choice == '3':
        break
    else:
        print('Please select correct option')