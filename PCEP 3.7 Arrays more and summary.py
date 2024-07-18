# A four-column/four-row table ‒ a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'

#while loop, gives 2 "*" (or any element as string)
i=2
while i >= 0:
    print("*")
    i-=2

# range funtion rnage(a, b) BEGINS with value of "a" but DOES NOT include the value of "b", outputs 2 copies of the string
for i in range(-1,1):
    print("#")

my_list=[0 for i in range(1,3)]
print(my_list)

my_list=[0,1,2,3]
x=1
for element in my_list:
    x*=element
print(x)
