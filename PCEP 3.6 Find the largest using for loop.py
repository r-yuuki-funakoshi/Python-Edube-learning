#Example1
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#Example2
my_list2=[1,2,6,5,56,4,3,5,7,5,4,35]
largest=my_list2[0]

for x in range(1, len(my_list2[1:])):
    if my_list2[x] > largest:
        largest=my_list2[x]
print("The largest number is: ", largest)
print("The position of the largest number", my_list2.index(largest))
