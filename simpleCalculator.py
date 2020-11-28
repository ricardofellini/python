#Calculator - Just to practice

# Function ADD
def add(a, b):
    return a + b

# Function SUBTRACT
def subtract(a, b):
    return a - b

# Function MULTIPLY
def multiply(a, b):
    return a * b

# Function DIVIDE
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Zero division error"

# Function POWER
def power(a, b):
    return a**b

# Function MAIN
def main():
    print("Select Operation")
    print("1.ADD")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")

    #Show the options and use INPUT numbers
    choice = input("Enter Choice(+,-,*,/,ˆ): ")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Conditions

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == "3":
        print(num1, '*', num2, "=", multiply(num1, num2))

    elif choice == "4":
        print(num1, '/', num2, "=", divide(num1, num2))

    elif choice == "5":
        print(num1, "ˆ", num2, "=", power(num1, num2))
    else:
        print("Invalid")
        main()
main()


