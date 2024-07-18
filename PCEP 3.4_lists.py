

# NOTE:  list can have multiple scalars (each of values in lists are scalars)
# It can stote different data types
#Numbers are assigned to each element of the list from 0 to N-1 (Where N is the total amount of elements)


numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("\nNew list content:", numbers)  # Printing current list content.

numbers[2]="Banana"
print("\nAnother new list content", numbers)

print(numbers[4]) #Accessing and printing one scalar separately
print(numbers) #Accessing the entire list
