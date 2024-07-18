# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number=max(number1, number2, number3)
Smallest_number=min(number1, number2, number3)
Largest_product=max(number1*number2, number1*number3, number2*number3)
Smallest_remainder=min(number1%number2, number1%number3, number2%number3)

# Print the result.
print("The largest number is:", largest_number)
print("The smallest number is:", Smallest_number)
print("The largest product is:", Largest_product)
print("The smallest remainder is:", Smallest_remainder)
