numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4) #list.append() inserts a value in () at the end of the list

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222) #list.insert(a,b) inserts a value b at position a
print(len(numbers))
print(numbers)

#
numbers.insert(1,333)
print(len(numbers))
print(numbers)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i+1)

print(my_list)

