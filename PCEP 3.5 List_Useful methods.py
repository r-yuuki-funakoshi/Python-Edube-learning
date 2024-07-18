#For loop and list

list_1=[1,2,3,4,5,6,7,8,9,10]
total=0
for i in range(len(list_1)):
    total+=list_1[i]

print(total)

#Other methods
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

print(fruits.count('tangerine')) #count the number of "tangerine" in the list

fruits.index('banana') #Find the first possible position of "banana" from position 0

fruits.index('banana', 4)  # Find next banana starting at position 4

print(fruits.reverse()) #Reverse the elements of the list in place
fruits

fruits.append('grape') #This is equivalent to a[len(a):]=[grape]
fruits

fruits.sort() 
fruits

print(fruits.pop())

fruits.extend("tangerine")
print(fruits)
#Extend the list by appending all the items from the iterable
#Equivalent to a[len(a):]=iterable
