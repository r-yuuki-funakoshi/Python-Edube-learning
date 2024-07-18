print("Practice excercise for module 3.2 section, loops")

#1 counts 0-10 nut only odd numbers
for x in range(0, 11):
    if x%2!=0:
        print("Odd number: ", x)
#2 Same result but use while
x=0
while True:
    if x==10:
        break
    x+=1
    if x%2!=0:
        print("Odd number: ", x)

#3 break and continue
for letter in "meowmeow@gmail.com":
    a="@"
    if letter==a:
        break
    print(letter)

#Replacing 4 with letter x using print function and continue statement
for digit in "703849479384654830274658490383648392":
    if digit=="4":
        print("x", end="") #first, print x after the program skip the current iteration and ignore 4
        continue #iteration continues to the next number
    print(digit, end="") #prints digits with replaced letters

