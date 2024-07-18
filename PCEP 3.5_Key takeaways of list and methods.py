#List takes anything thata can be stored
my_list = [1, None, True, "I am a string", 256, 0]

#List can be amended
my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0

my_list[1] = '?' #This is equivalent to my_list.insert(1, '?')
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

#Lists can be NESTED
my_list = [1, 'a', ["list", 64, [0, 1], False]]

#list can be iterable using for loop
my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)

#Using for loop to obtain multiple results and make a new list of results
Numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
Numbers2=[]
Numbers3=[]

add=0
for i in Numbers:
    add+=i
    Numbers2.append(add)
print(Numbers2)

product=1
for x in Numbers2:
    product*=x
    Numbers3.append(product)
print(Numbers3)



