"""Electricity_Bill_Calculator

Menu-driven program that calculates electricity bills using slab rates,
adds 5% VAT, and stores every bill in bills.txt.
"""

BILL_FILE = "bills.txt"
VAT_RATE = 0.05


def calculate_units(previous_reading, current_reading):
    """Units Consumed = Current Reading - Previous Reading."""
    return current_reading - previous_reading


def calculate_energy_charge(units):
    """Slab rates:
    First 100 units      -> 5 Tk/unit
    Next 100 (101-200)   -> 7 Tk/unit
    Above 200 units      -> 10 Tk/unit
    """
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10


def calculate_vat(energy_charge):
    """VAT = 5% of Energy Charge."""
    return energy_charge * VAT_RATE


def calculate_total_bill(energy_charge, vat):
    """Total Bill = Energy Charge + VAT."""
    return energy_charge + vat


def read_positive_number(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue
        if number <= 0:
            print("Invalid input! Value must be a positive number.")
            continue
        return number


def read_non_empty(prompt):
    """Keep asking until the user enters a non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid input! This field cannot be empty.")


def add_customer_bill():
    customer_name = read_non_empty("Enter Customer Name: ")
    meter_number = read_non_empty("Enter Meter Number: ")

    previous_reading = read_positive_number("Enter Previous Reading: ")
    while True:
        current_reading = read_positive_number("Enter Current Reading: ")
        if current_reading > previous_reading:
            break
        print("Invalid input! Current Reading must be greater than Previous Reading.")

    units = calculate_units(previous_reading, current_reading)
    energy_charge = calculate_energy_charge(units)
    vat = calculate_vat(energy_charge)
    total_bill = calculate_total_bill(energy_charge, vat)

    print("\n----------- Electricity Bill -----------")
    print(f"Customer Name   : {customer_name}")
    print(f"Meter Number    : {meter_number}")
    print(f"Units Consumed  : {units:.2f}")
    print(f"Energy Charge   : {energy_charge:.2f} Tk")
    print(f"VAT (5%)        : {vat:.2f} Tk")
    print(f"Total Bill      : {total_bill:.2f} Tk")
    print("----------------------------------------")

    try:
        with open(BILL_FILE, "a") as file:
            file.write(
                f"Customer Name: {customer_name}, Meter Number: {meter_number}, "
                f"Units: {units:.2f}, Total Bill: {total_bill:.2f} Tk\n"
            )
        print("Bill saved successfully!")
    except OSError as error:
        print(f"Error: could not save the bill ({error}).")


def view_all_bills():
    try:
        with open(BILL_FILE, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("No bills found yet. Add a customer bill first.")
        return
    except OSError as error:
        print(f"Error: could not read the bills ({error}).")
        return

    if not content.strip():
        print("No bills found yet. Add a customer bill first.")
        return

    print("\n------------ Bill History ------------")
    print(content, end="")
    print("--------------------------------------")


def main():
    while True:
        print("\n===== Electricity Bill Calculator =====")
        print("1. Add Customer Bill")
        print("2. View All Bills")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_customer_bill()
        elif choice == "2":
            view_all_bills()
        elif choice == "3":
            print("Thank you for using Electricity Bill Calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()
