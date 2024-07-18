#Remove repeated numbers to create a new list
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for x in my_list:
    if x not in unique_list:
        unique_list.append(x)

print("The list with unique non-repeated elements only:")
print(unique_list)

#Include the same value
list1=[1,2,3,4,3,4,5,6,7,8,9,7,8,7,6,5,6,4,3,2,3,2,4,5,6,7,8,7,6,5,4,5,3,2,3,1]
same_list=[]

for i in list1:
    if i == 2:
        same_list.append(i)

print(same_list)
print("The length of the list1: ", len(list1))
print("The length of the new list: ", len(same_list))

