# Employee Payroll & Performance Evaluation System
# Python Programming Fundamentals

def get_positive_number(prompt):
    """Get a positive numeric value from the user."""
    while True:
        try:
            value = float(input(prompt))

            if value >= 0:
                return value

            print("Please enter a positive value.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_performance_score():
    """Get a performance score between 0 and 100."""
    while True:
        try:
            score = float(input("Performance Score (0-100): "))

            if 0 <= score <= 100:
                return score

            print("Score must be between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate_payroll(
    basic_salary,
    overtime_hours,
    overtime_rate,
    tax_percentage
):
    """Calculate overtime, gross salary, tax and net salary."""

    # Arithmetic operators
    overtime_pay = overtime_hours * overtime_rate
    gross_salary = basic_salary + overtime_pay
    tax_amount = gross_salary * (tax_percentage / 100)
    net_salary = gross_salary - tax_amount

    # Other arithmetic operators
    remainder = int(gross_salary) % 100
    power_example = 2 ** 3
    payment_cycles = int(gross_salary) // 1000

    return (
        overtime_pay,
        gross_salary,
        tax_amount,
        net_salary,
        remainder,
        power_example,
        payment_cycles
    )


def performance_status(score):
    """Use ternary operator for performance eligibility."""

    status = (
        "Eligible for Bonus"
        if score >= 80
        else "Not Eligible"
    )

    return status


def calculate_grade(score):
    """Calculate employee grade."""

    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "C"


def main():
    print("=" * 50)
    print("       EMPLOYEE PAYROLL SYSTEM")
    print("=" * 50)

    # Employee information
    employee_id = input("Employee ID: ")
    employee_name = input("Employee Name: ")

    basic_salary = get_positive_number("Basic Salary: ")
    overtime_hours = get_positive_number("Overtime Hours: ")
    overtime_rate = get_positive_number("Overtime Rate: ")
    performance_score = get_performance_score()
    tax_percentage = get_positive_number("Tax Percentage: ")

    # Calculate payroll
    (
        overtime_pay,
        gross_salary,
        tax_amount,
        net_salary,
        remainder,
        power_example,
        payment_cycles
    ) = calculate_payroll(
        basic_salary,
        overtime_hours,
        overtime_rate,
        tax_percentage
    )

    # Ternary operator
    status = performance_status(performance_score)

    # Employee grade
    grade = calculate_grade(performance_score)

    # Assignment operators demonstration
    salary_update = net_salary

    # += Add annual bonus
    annual_bonus = 500
    salary_update += annual_bonus

    # -= Deduct insurance
    insurance = 100
    salary_update -= insurance

    # *= Performance multiplier
    if performance_score >= 80:
        salary_update *= 1.05
    else:
        salary_update *= 1.02

    # /= Calculate monthly salary
    monthly_salary = salary_update
    monthly_salary /= 12

    # //= Complete payment cycles
    cycles = int(gross_salary)
    cycles //= 1000

    # %= Remaining bonus allocation
    bonus_allocation = int(gross_salary)
    bonus_allocation %= 1000

    # Annual salary
    annual_salary = monthly_salary * 12

    # Output
    print("\n")
    print("=" * 50)
    print("          EMPLOYEE PAYROLL REPORT")
    print("=" * 50)

    print(f"\nEmployee ID        : {employee_id}")
    print(f"Employee Name      : {employee_name}")

    print(f"\nBasic Salary       : ${basic_salary:,.2f}")
    print(f"Overtime Pay       : ${overtime_pay:,.2f}")
    print(f"Gross Salary       : ${gross_salary:,.2f}")
    print(f"Tax Amount         : ${tax_amount:,.2f}")
    print(f"Net Salary         : ${net_salary:,.2f}")

    print(f"\nPerformance Score  : {performance_score:.0f}")
    print(f"Performance Status : {status}")
    print(f"Employee Grade     : {grade}")

    print(f"\nAnnual Bonus       : ${annual_bonus:,.2f}")
    print(f"Insurance Deduction: ${insurance:,.2f}")

    print(f"Monthly Salary     : ${monthly_salary:,.2f}")
    print(f"Annual Salary      : ${annual_salary:,.2f}")

    print("\n--- Operator Demonstration ---")
    print(f"Modulus (%)        : {remainder}")
    print(f"Exponent (**)      : {power_example}")
    print(f"Floor Division (//): {payment_cycles}")
    print(f"Payment Cycles     : {cycles}")
    print(f"Bonus Remainder    : {bonus_allocation}")

    print("\n" + "=" * 50)
    print("          END OF REPORT")
    print("=" * 50)


# Program starts here
if __name__ == "__main__":
    main()