import math

def investment_calculation():
    amount = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (in percentage): ")) / 100
    years = int(input("Enter the number of years for investment: "))
    interest = input("Enter 'simple' or 'compound' interest: ")

    if interest.lower() == "simple":
        total_amount = amount * (1 + interest_rate * years)
    elif interest.lower() == "compound":
        total_amount = amount * math.pow((1 + interest_rate), years)
    else:
        print("Invalid interest type. Please enter either 'simple' or 'compound'.")
        return

    print("The total amount after {} years at {}% {} interest will be: {}".format(years, interest_rate * 100, interest, total_amount))


def bond_calculation():
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (in percentage): ")) / 100
    months = int(input("Enter the number of months to repay the bond: "))

    monthly_interest_rate = interest_rate / 12
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow(1 + monthly_interest_rate, -months))

    print("The monthly repayment amount for the bond will be: {}".format(repayment))


def main():
    print("***********************************************************************")
    print("**********Welcome to the FUTURE LEADERS Finance Calculator!************")
    print("***********************************************************************")
    print("\n**** MENU****")
    print("\nPlease select an option:")
    print("1. Investment")
    print("2. Bond")

    choice = input("Enter your choice (investment or bond): ")

    if choice.lower() == "investment":
        investment_calculation()
    elif choice.lower() == "bond":
        bond_calculation()
    else:
        print("Invalid choice. Please enter either investment or bond.")


if __name__ == "__main__":
    main()
