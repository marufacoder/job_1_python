"""Student Result Calculator

A menu-driven program that takes a student's name, roll number and marks
for 5 subjects, validates the marks, and calculates the total, average,
grade and pass/fail result. Results are stored in a list.
"""

NUM_SUBJECTS = 5
PASS_MARK = 33

# List used to store all student results
results = []


# ---------------------------------------------------------------------------
# Calculation functions
# ---------------------------------------------------------------------------
def calculate_total(marks):
    """Total Marks = sum of all subject marks."""
    return sum(marks)


def calculate_average(total, num_subjects=NUM_SUBJECTS):
    """Average Marks = Total Marks / Number of Subjects."""
    return total / num_subjects


def calculate_result(marks):
    """Fail if any subject mark is below 33, otherwise Pass."""
    for mark in marks:
        if mark < PASS_MARK:
            return "Fail"
    return "Pass"


def calculate_grade(average):
    """Return the grade based on the average marks."""
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 33:
        return "D"
    else:
        return "F"


# ---------------------------------------------------------------------------
# Input helpers with validation
# ---------------------------------------------------------------------------
def get_non_empty_input(prompt):
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid input: this field cannot be empty. Please try again.")


def get_valid_mark(subject_number):
    """Keep asking until the user enters a valid mark between 0 and 100."""
    while True:
        raw = input(f"Enter marks for Subject {subject_number} (0-100): ").strip()
        try:
            mark = float(raw)
        except ValueError:
            print("Invalid input: please enter a numeric value.")
            continue

        if 0 <= mark <= 100:
            return mark
        print("Invalid input: marks must be between 0 and 100.")


# ---------------------------------------------------------------------------
# Menu operations
# ---------------------------------------------------------------------------
def add_student_result():
    """Take student details, calculate the result and store it in the list."""
    print("\n--- Add Student Result ---")
    name = get_non_empty_input("Enter Student Name: ")
    roll = get_non_empty_input("Enter Roll Number: ")

    # Prevent duplicate roll numbers
    for record in results:
        if record["roll"] == roll:
            print(f"Invalid input: a result for Roll Number {roll} already exists.")
            return

    marks = [get_valid_mark(i) for i in range(1, NUM_SUBJECTS + 1)]

    total = calculate_total(marks)
    average = calculate_average(total)
    grade = calculate_grade(average)
    result = calculate_result(marks)

    results.append(
        {
            "name": name,
            "roll": roll,
            "total": total,
            "average": average,
            "grade": grade,
            "result": result,
        }
    )

    print(f"\nSuccess: result for {name} (Roll {roll}) was added successfully!")
    print(f"Total: {total:.2f} | Average: {average:.2f} | Grade: {grade} | Result: {result}")


def view_all_results():
    """Display all saved results and the total number of results saved."""
    print("\n--- All Student Results ---")
    if not results:
        print("No results saved yet.")
        print("Total results saved: 0")
        return

    header = (
        f"{'No.':<5}{'Name':<20}{'Roll':<12}{'Total':<10}"
        f"{'Average':<10}{'Grade':<8}{'Result':<8}"
    )
    print(header)
    print("-" * len(header))

    for index, r in enumerate(results, start=1):
        print(
            f"{index:<5}{r['name']:<20}{r['roll']:<12}{r['total']:<10.2f}"
            f"{r['average']:<10.2f}{r['grade']:<8}{r['result']:<8}"
        )

    print("-" * len(header))
    print(f"Total results saved: {len(results)}")


def show_menu():
    print("\n===== Student Result Calculator =====")
    print("1. Add Student Result")
    print("2. View All Results")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student_result()
        elif choice == "2":
            view_all_results()
        elif choice == "3":
            print("\nThank you for using Student Result Calculator. Goodbye!")
            break
        else:
            print("Invalid choice: please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
