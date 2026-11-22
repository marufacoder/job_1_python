"""Employee_Salary_Calculator

A menu-driven program that calculates employee salaries (house rent,
medical allowance, gross salary, tax and net salary) and stores the
records in a list.
"""

import math

# List that stores all salary records (each record is a dictionary)
salary_records = []


# ---------------------------------------------------------------------------
# Calculation functions
# ---------------------------------------------------------------------------
def calculate_house_rent(basic_salary):
    """House Rent = 40% of Basic Salary."""
    return basic_salary * 0.40


def calculate_medical_allowance(basic_salary):
    """Medical Allowance = 10% of Basic Salary."""
    return basic_salary * 0.10


def calculate_gross_salary(basic_salary, house_rent, medical_allowance):
    """Gross Salary = Basic Salary + House Rent + Medical Allowance."""
    return basic_salary + house_rent + medical_allowance


def calculate_tax(gross_salary):
    """Automatic tax calculation based on gross salary.

    50000 and above  -> 10% tax
    30000 - 49999    -> 5% tax
    below 30000      -> no tax
    """
    if gross_salary >= 50000:
        return gross_salary * 0.10
    elif gross_salary >= 30000:
        return gross_salary * 0.05
    return 0.0


def calculate_net_salary(gross_salary, tax):
    """Net Salary = Gross Salary - Tax."""
    return gross_salary - tax


# ---------------------------------------------------------------------------
# Input helpers (with validation)
# ---------------------------------------------------------------------------
def get_non_empty_input(prompt, field_name):
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"Invalid input: {field_name} cannot be empty. Please try again.")


def get_employee_id():
    """Ask for an Employee ID and make sure it has not been used already."""
    while True:
        emp_id = get_non_empty_input("Enter Employee ID: ", "Employee ID")
        if any(record["id"].lower() == emp_id.lower() for record in salary_records):
            print(f"Invalid input: Employee ID '{emp_id}' already exists. Please use a different ID.")
        else:
            return emp_id


def get_basic_salary():
    """Ask for the Basic Salary and validate that it is a positive number."""
    while True:
        value = input("Enter Basic Salary: ").strip()
        try:
            salary = float(value)
        except ValueError:
            print("Invalid input: Basic Salary must be a number. Please try again.")
            continue

        if math.isnan(salary) or math.isinf(salary):
            print("Invalid input: Basic Salary must be a valid number. Please try again.")
        elif salary <= 0:
            print("Invalid input: Basic Salary must be a positive number. Please try again.")
        else:
            return salary


# ---------------------------------------------------------------------------
# Menu actions
# ---------------------------------------------------------------------------
def add_employee_salary():
    """Take employee details, calculate the salary and save the record."""
    print("\n--- Add Employee Salary ---")
    name = get_non_empty_input("Enter Employee Name: ", "Employee Name")
    emp_id = get_employee_id()
    designation = get_non_empty_input("Enter Designation: ", "Designation")
    basic_salary = get_basic_salary()

    house_rent = calculate_house_rent(basic_salary)
    medical_allowance = calculate_medical_allowance(basic_salary)
    gross_salary = calculate_gross_salary(basic_salary, house_rent, medical_allowance)
    tax = calculate_tax(gross_salary)
    net_salary = calculate_net_salary(gross_salary, tax)

    record = {
        "name": name,
        "id": emp_id,
        "designation": designation,
        "gross": gross_salary,
        "tax": tax,
        "net": net_salary,
    }
    salary_records.append(record)

    print("\nSalary calculated and saved successfully!")
    print(f"  Basic Salary      : {basic_salary:,.2f}")
    print(f"  House Rent (40%)  : {house_rent:,.2f}")
    print(f"  Medical (10%)     : {medical_allowance:,.2f}")
    print(f"  Gross Salary      : {gross_salary:,.2f}")
    print(f"  Tax               : {tax:,.2f}")
    print(f"  Net Salary        : {net_salary:,.2f}")


def view_all_records():
    """Display all saved salary records and the total count."""
    print("\n--- All Salary Records ---")
    if not salary_records:
        print("No salary records found.")
    else:
        header = f"{'No.':<5}{'Name':<20}{'ID':<12}{'Gross Salary':>15}{'Tax':>12}{'Net Salary':>15}"
        print(header)
        print("-" * len(header))
        for index, rec in enumerate(salary_records, start=1):
            print(
                f"{index:<5}{rec['name']:<20}{rec['id']:<12}"
                f"{rec['gross']:>15,.2f}{rec['tax']:>12,.2f}{rec['net']:>15,.2f}"
            )
        print("-" * len(header))
    print(f"Total salary records saved: {len(salary_records)}")


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------
def main():
    print("=" * 40)
    print("      EMPLOYEE SALARY CALCULATOR")
    print("=" * 40)

    while True:
        print("\nMenu:")
        print("  1. Add Employee Salary")
        print("  2. View All Records")
        print("  3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_employee_salary()
        elif choice == "2":
            view_all_records()
        elif choice == "3":
            print("\nThank you for using Employee Salary Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
