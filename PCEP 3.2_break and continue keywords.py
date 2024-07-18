


#BREAK - exits the loop immediately, and unconditionally ends the loop's operation; the program begins to execute the nearest instruction after the loop's body;
#CONTINUE - behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.

print("The break instruction:")
for i in range(0, 10, 2):
    if i==7:
        break #Simply breaks the current iteration
    print("Program execution stopped", i)


print("The continue instruction:")
for i in range(0, 10, 2):
    if i==7:
        continue #Breaks the current iteration and  CONTINUES with a new one.
    print("Program continued", i)

list=["banana", "apple", "meowmeow", "cow"]

for x in list:
    if x=="apple":
        continue
    print(x) #"apple" will not be printed nut execution continues
