import math
#BREAK STATEMENT
largest_number = -math.inf
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

#CONTINUE STATEMENT
largest_number = -math.inf
counter = 0

number = int(input("Enter a number or type -1 to end program: ")) #if this input function was after the while True statement, the iteration skips "-1" and continues...IT NEVER STOPS

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter!=0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

  
