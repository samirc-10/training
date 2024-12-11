try:
    # Ask the user for three numbers
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))

    # Check which number is the biggest
    if first_number >= second_number and first_number >= third_number:
        greatest_number = first_number
    elif second_number >= first_number and second_number >= third_number:
        greatest_number = second_number
    else:
        greatest_number = third_number

    # Show the biggest number
    print("The greatest number is:", greatest_number)

except ValueError:
    # Show an error if the input is not a number
    print("Invalid input! Please enter valid numbers.")



